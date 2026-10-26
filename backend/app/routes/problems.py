import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Problem, Attempt
from ..schemas import ProblemSummary, ProblemDetail

router = APIRouter(prefix="/api/problems", tags=["Problems"])

@router.get("", response_model=List[ProblemSummary])
def list_problems(db: Session = Depends(get_db)):
    problems = db.query(Problem).order_by(Problem.order_index).all()
    result = []
    for p in problems:
        # Check if user has solved this problem
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
                attempt_count=attempt_count
            )
        )
    return result

@router.get("/{problem_id}", response_model=ProblemDetail)
def get_problem(problem_id: str, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    solved = db.query(Attempt).filter(Attempt.problem_id == problem.id, Attempt.is_solved == True).first() is not None

    test_cases_data = json.loads(problem.test_cases) if problem.test_cases else []
    edge_cases_data = json.loads(problem.edge_cases) if problem.edge_cases else []

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
        order_index=problem.order_index,
        is_solved=solved
    )
