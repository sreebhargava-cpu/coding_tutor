import json
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base, SessionLocal
from .models import Problem
from .problems_data import PREDEFINED_PROBLEMS
from .routes import problems, tutor, progress

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

def seed_database():
    """Seeds predefined problems if the database is fresh."""
    db = SessionLocal()
    try:
        for p_data in PREDEFINED_PROBLEMS:
            existing = db.query(Problem).filter(Problem.id == p_data["id"]).first()
            if not existing:
                problem = Problem(
                    id=p_data["id"],
                    title=p_data["title"],
                    difficulty=p_data["difficulty"],
                    category=p_data["category"],
                    description=p_data["description"],
                    learning_objective=p_data["learning_objective"],
                    starter_code=p_data["starter_code"],
                    function_name=p_data["function_name"],
                    test_cases=json.dumps(p_data["test_cases"]),
                    solution_approach=p_data["solution_approach"],
                    edge_cases=json.dumps(p_data.get("edge_cases", [])),
                    order_index=p_data.get("order_index", 0)
                )
                db.add(problem)
        db.commit()
        logger.info("Database seeded with predefined problems.")
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables and seed problems
    Base.metadata.create_all(bind=engine)
    seed_database()
    yield
    # Shutdown

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for AI-Powered Adaptive Coding Tutor",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for local dev servers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In development allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# Include routers
app.include_router(problems.router)
app.include_router(tutor.router)
app.include_router(progress.router)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# Mount built frontend static files if present
frontend_dist = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="frontend")
else:
    @app.get("/")
    def root():
        return {
            "status": "online",
            "service": settings.PROJECT_NAME,
            "docs_url": "/docs"
        }

