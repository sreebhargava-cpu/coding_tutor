from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from ..database import get_db
from ..models import Problem, Attempt, Weakness, TutorInteraction
from ..schemas import RecordAttemptRequest, ProgressSummaryResponse, DifficultyStat

router = APIRouter(prefix="/api/progress", tags=["Progress"])

CATEGORY_DISPLAY_NAMES = {
    "indexing": "List & String Indexing",
    "loops": "Loop Boundaries & Iteration",
    "conditional_logic": "Conditional Logic & Boolean Flags",
    "type_error": "Data Types & Incompatible Operations",
    "syntax_error": "Python Syntax & Indentation",
    "variable_error": "Variable Scope & Naming",
    "functions": "Function Arguments & Return Values",
    "data_structures": "Dictionaries & Sets",
    "logical_error": "General Logic & Algorithms",
    "edge_case": "Boundary & Edge Case Handling",
}

@router.post("/attempt")
def record_attempt(payload: RecordAttemptRequest, db: Session = Depends(get_db)):
    is_solved = (payload.status == "passed")

    attempt = Attempt(
        problem_id=payload.problem_id,
        code=payload.code,
        status=payload.status,
        error_type=payload.error_type,
        error_message=payload.error_message,
        error_line=payload.error_line,
        bug_category=payload.bug_category or "logical_error",
        passed_tests=payload.passed_tests,
        total_tests=payload.total_tests,
        execution_time_ms=payload.execution_time_ms,
        hints_used=payload.hints_used,
        is_solved=is_solved,
        created_at=datetime.utcnow()
    )
    db.add(attempt)

    # Track recurring weakness if an error or bug occurred
    if payload.status != "passed" and payload.bug_category:
        cat = payload.bug_category.lower()
        weakness = db.query(Weakness).filter(Weakness.category == cat).first()
        if not weakness:
            display = CATEGORY_DISPLAY_NAMES.get(cat, cat.replace("_", " ").title())
            weakness = Weakness(category=cat, display_name=display, mistake_count=1, last_occurred=datetime.utcnow())
            db.add(weakness)
        else:
            weakness.mistake_count += 1
            weakness.last_occurred = datetime.utcnow()

    db.commit()
    return {"status": "success", "attempt_id": attempt.id, "is_solved": is_solved}

@router.get("/summary", response_model=ProgressSummaryResponse)
def get_progress_summary(db: Session = Depends(get_db)):
    total_problems = db.query(Problem).count()
    total_attempts = db.query(Attempt).count()

    # Problems attempted
    attempted_ids = db.query(Attempt.problem_id).distinct().all()
    problems_attempted = len(attempted_ids)

    # Problems solved
    solved_ids = db.query(Attempt.problem_id).filter(Attempt.is_solved == True).distinct().all()
    problems_solved = len(solved_ids)

    completion_rate = (problems_solved / total_problems * 100) if total_problems > 0 else 0.0
    successful_attempts = db.query(Attempt).filter(Attempt.is_solved == True).count()
    attempt_success_rate = (successful_attempts / total_attempts * 100) if total_attempts > 0 else 0.0

    # Common difficulties breakdown
    weaknesses = db.query(Weakness).order_by(Weakness.mistake_count.desc()).all()
    difficulty_stats = []
    for w in weaknesses:
        difficulty_stats.append(
            DifficultyStat(
                category=w.category,
                display_name=w.display_name,
                count=w.mistake_count
            )
        )

    # If no weakness records yet, populate default categories with zero count for clean chart display
    if not difficulty_stats:
        for cat, display in list(CATEGORY_DISPLAY_NAMES.items())[:5]:
            difficulty_stats.append(DifficultyStat(category=cat, display_name=display, count=0))

    # Identify top recurring weaknesses
    top_weaknesses = [w.display_name for w in weaknesses[:3] if w.mistake_count > 0]

    # Generate suggested focus
    if top_weaknesses:
        suggested_focus = f"Focus practice on {top_weaknesses[0]}. Pay close attention to boundaries, indices, and assumptions."
    elif problems_solved == total_problems and total_problems > 0:
        suggested_focus = "Outstanding! You have solved all curriculum problems. Try challenging yourself with custom edge cases."
    else:
        suggested_focus = "Start with beginner problems on Variables and Conditions to build confidence."

    # Recent attempts
    recent = db.query(Attempt).order_by(Attempt.created_at.desc()).limit(10).all()
    recent_list = []
    for a in recent:
        prob = db.query(Problem).filter(Problem.id == a.problem_id).first()
        recent_list.append({
            "id": a.id,
            "problem_id": a.problem_id,
            "problem_title": prob.title if prob else a.problem_id,
            "status": a.status,
            "bug_category": a.bug_category,
            "passed_tests": a.passed_tests,
            "total_tests": a.total_tests,
            "hints_used": a.hints_used,
            "is_solved": a.is_solved,
            "timestamp": a.created_at.strftime("%b %d, %H:%M") if a.created_at else ""
        })

    return ProgressSummaryResponse(
        problems_attempted=problems_attempted,
        problems_solved=problems_solved,
        total_problems=total_problems,
        completion_rate_percent=round(completion_rate, 1),
        attempt_success_rate_percent=round(attempt_success_rate, 1),
        success_rate_percent=round(completion_rate, 1),
        total_attempts=total_attempts,
        common_difficulties=difficulty_stats,
        recurring_weaknesses=top_weaknesses,
        suggested_focus=suggested_focus,
        recent_attempts=recent_list
    )

@router.post("/reset")
def reset_progress(db: Session = Depends(get_db)):
    db.query(Attempt).delete()
    db.query(Weakness).delete()
    db.query(TutorInteraction).delete()
    db.commit()
    return {"status": "success", "message": "Progress reset successfully"}
