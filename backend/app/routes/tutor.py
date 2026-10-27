import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Problem, Attempt, Weakness, TutorInteraction
from ..schemas import (
    HintRequest,
    HintResponse,
    ExplainErrorRequest,
    ExplainErrorResponse,
    ExplainConceptRequest,
    ExplainConceptResponse,
    CodeQualityRequest,
    CodeQualityResponse,
    EdgeCaseRequest,
    EdgeCaseResponse
)
from ..ai_service import (
    generate_socratic_hint,
    explain_runtime_error,
    explain_concept_in_context,
    coach_code_quality,
    generate_edge_case_challenges
)

router = APIRouter(prefix="/api/tutor", tags=["Tutor"])

@router.post("/hint", response_model=HintResponse)
def get_socratic_hint(payload: HintRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == payload.problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Fetch top weaknesses for personalization
    weaknesses = db.query(Weakness).order_by(Weakness.mistake_count.desc()).limit(3).all()
    weakness_names = [w.category for w in weaknesses]

    exec_dict = payload.execution_result.dict() if payload.execution_result else None

    # Check if Gemini API is available
    from ..ai_service import get_gemini_client
    gemini_client = get_gemini_client()

    # If Gemini is offline/unavailable:
    if not gemini_client:
        # Check if preset problem with curated hints
        stored_hints = json.loads(problem.hints) if problem.hints else []
        if stored_hints and getattr(problem, "is_preset", True):
            level = max(1, min(3, payload.current_hint_level))
            hint_idx = level - 1
            hint_text = stored_hints[hint_idx] if hint_idx < len(stored_hints) else stored_hints[-1]
            titles = {1: "Curated Nudge", 2: "Focused Direction", 3: "Specific Clue"}
            response = HintResponse(
                bug_category="preset_curated",
                hint_level=level,
                hint_title=titles.get(level, f"Curated Hint {level}"),
                socratic_question="Have you considered how this step relates to the problem rules?",
                hint_body=hint_text,
                targeted_line=None,
                should_reveal_solution=False,
                next_hint_available=(level < len(stored_hints))
            )
        else:
            # Custom problem offline: honest explanation, do not fake
            raise HTTPException(
                status_code=503,
                detail="AI Tutoring is currently offline. AI-generated coaching is unavailable for custom problems without Gemini connection."
            )
    else:
        # Socratic Adaptive Hint generation via Gemini
        response = generate_socratic_hint(
            problem_title=problem.title,
            problem_desc=problem.description,
            learning_obj=problem.learning_objective,
            student_code=payload.code,
            execution_result=exec_dict,
            hint_level=payload.current_hint_level,
            previous_hints=payload.previous_hints,
            student_weaknesses=weakness_names
        )

    # Record tutor interaction
    interaction = TutorInteraction(
        problem_id=payload.problem_id,
        interaction_type="hint",
        hint_level=response.hint_level,
        student_code=payload.code,
        ai_response=json.dumps(response.dict())
    )
    db.add(interaction)
    db.commit()

    return response

@router.post("/explain-error", response_model=ExplainErrorResponse)
def explain_error(payload: ExplainErrorRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == payload.problem_id).first()
    problem_title = problem.title if problem else "Python Problem"

    response = explain_runtime_error(
        problem_title=problem_title,
        student_code=payload.code,
        error_type=payload.error_type,
        error_message=payload.error_message,
        error_line=payload.error_line
    )

    interaction = TutorInteraction(
        problem_id=payload.problem_id,
        interaction_type="explain_error",
        student_code=payload.code,
        ai_response=json.dumps(response.dict())
    )
    db.add(interaction)
    db.commit()

    return response

@router.post("/explain-concept", response_model=ExplainConceptResponse)
def explain_concept(payload: ExplainConceptRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == payload.problem_id).first()
    problem_title = problem.title if problem else "Python Problem"

    response = explain_concept_in_context(
        problem_title=problem_title,
        student_code=payload.code,
        selected_text=payload.selected_text,
        concept_name=payload.concept_name
    )

    interaction = TutorInteraction(
        problem_id=payload.problem_id,
        interaction_type="explain_concept",
        student_code=payload.code,
        ai_response=json.dumps(response.dict())
    )
    db.add(interaction)
    db.commit()

    return response

@router.post("/code-quality", response_model=CodeQualityResponse)
def get_code_quality(payload: CodeQualityRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == payload.problem_id).first()
    problem_title = problem.title if problem else "Python Problem"

    response = coach_code_quality(
        problem_title=problem_title,
        student_code=payload.code
    )

    interaction = TutorInteraction(
        problem_id=payload.problem_id,
        interaction_type="quality",
        student_code=payload.code,
        ai_response=json.dumps(response.dict())
    )
    db.add(interaction)
    db.commit()

    return response

@router.post("/edge-cases", response_model=EdgeCaseResponse)
def get_edge_cases(payload: EdgeCaseRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == payload.problem_id).first()
    problem_title = problem.title if problem else "Python Problem"
    predefined = json.loads(problem.edge_cases) if (problem and problem.edge_cases) else None

    response = generate_edge_case_challenges(
        problem_title=problem_title,
        student_code=payload.code,
        predefined_edge_cases=predefined
    )

    interaction = TutorInteraction(
        problem_id=payload.problem_id,
        interaction_type="edge_case",
        student_code=payload.code,
        ai_response=json.dumps(response.dict())
    )
    db.add(interaction)
    db.commit()

    return response
