import json
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Problem, Attempt
from ..schemas import (
    ProblemSummary, 
    ProblemDetail, 
    CustomProblemGenerateRequest, 
    CustomProblemSaveRequest
)
from ..ai_service import generate_custom_problem

router = APIRouter(prefix="/api/problems", tags=["Problems"])

@router.get("", response_model=List[ProblemSummary])
def list_problems(db: Session = Depends(get_db)):
    problems = db.query(Problem).order_by(Problem.order_index).all()
    result = []
    for p in problems:
        solved = db.query(Attempt).filter(Attempt.problem_id == p.id, Attempt.is_solved == True).first() is not None
        attempt_count = db.query(Attempt).filter(Attempt.problem_id == p.id).count()
        result.append(
            ProblemSummary(
                id=p.id,
                title=p.title,
                difficulty=p.difficulty,
                category=p.category,
                learning_objective=p.learning_objective,
                order_index=p.order_index,
                is_solved=solved,
                attempt_count=attempt_count,
                is_preset=getattr(p, "is_preset", True)
            )
        )
    return result

@router.post("/custom/generate")
def create_custom_problem(payload: CustomProblemGenerateRequest):
    """Generate a custom coding challenge via Gemini based on natural language prompt."""
    if not payload.description.strip():
        raise HTTPException(status_code=400, detail="Description prompt cannot be empty.")
    
    generated = generate_custom_problem(payload.description)
    if not generated:
        raise HTTPException(
            status_code=503, 
            detail="AI generation is currently unavailable. Please verify API key configuration or try again."
        )
    
    # Assign a temporary preview id
    generated["id"] = f"custom_{uuid.uuid4().hex[:8]}"
    return generated

@router.post("/custom/save")
def save_custom_problem(payload: CustomProblemSaveRequest, db: Session = Depends(get_db)):
    """Save a validated custom problem to the library as a first-class challenge."""
    problem_id = payload.id if payload.id and payload.id.startswith("custom_") else f"custom_{uuid.uuid4().hex[:8]}"
    
    # Check if duplicate save
    existing = db.query(Problem).filter(Problem.id == problem_id).first()
    if existing:
        return {"status": "already_saved", "id": existing.id, "title": existing.title}

    # Determine next order index
    max_order = db.query(Problem).count()

    problem = Problem(
        id=problem_id,
        title=payload.title,
        difficulty=payload.difficulty,
        category=payload.category,
        description=payload.description,
        learning_objective=payload.learning_objective,
        starter_code=payload.starter_code,
        function_name=payload.function_name,
        test_cases=json.dumps([tc.dict() for tc in payload.test_cases]),
        solution_approach=payload.solution_approach or "",
        edge_cases=json.dumps(payload.edge_cases or []),
        order_index=max_order + 1,
        is_preset=False,
        hints=json.dumps(payload.hints or [])
    )
    db.add(problem)
    db.commit()
    return {"status": "saved", "id": problem.id, "title": problem.title}

@router.delete("/{problem_id}")
def delete_problem(problem_id: str, db: Session = Depends(get_db)):
    """Delete a custom problem. Preset problems cannot be deleted."""
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    if getattr(problem, "is_preset", True):
        raise HTTPException(
            status_code=403, 
            detail="Preset curriculum problems cannot be deleted. Only custom problems can be deleted."
        )
    
    # Delete problem and its cascading attempts
    attempts_count = db.query(Attempt).filter(Attempt.problem_id == problem_id).count()
    db.delete(problem)
    db.commit()
    
    return {
        "status": "deleted", 
        "problem_id": problem_id, 
        "deleted_attempts_count": attempts_count,
        "message": f"Custom problem deleted along with its {attempts_count} attempt records."
    }

@router.get("/{problem_id}", response_model=ProblemDetail)
def get_problem(problem_id: str, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    solved = db.query(Attempt).filter(Attempt.problem_id == problem.id, Attempt.is_solved == True).first() is not None

    test_cases_data = json.loads(problem.test_cases) if problem.test_cases else []
    edge_cases_data = json.loads(problem.edge_cases) if problem.edge_cases else []
    hints_data = json.loads(problem.hints) if problem.hints else []

    return ProblemDetail(
        id=problem.id,
        title=problem.title,
        difficulty=problem.difficulty,
        category=problem.category,
        description=problem.description,
        learning_objective=problem.learning_objective,
        starter_code=problem.starter_code,
        function_name=problem.function_name,
        test_cases=test_cases_data,
        edge_cases=edge_cases_data,
        hints=hints_data,
        is_preset=getattr(problem, "is_preset", True),
        order_index=problem.order_index,
        is_solved=solved
    )
