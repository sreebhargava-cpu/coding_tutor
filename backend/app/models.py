from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Problem(Base):
    __tablename__ = "problems"

    id = Column(String(50), primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    difficulty = Column(String(20), nullable=False)  # Beginner, Intermediate, Advanced
    category = Column(String(50), nullable=False)    # Variables, Conditions, Loops, Lists, etc.
    description = Column(Text, nullable=False)
    learning_objective = Column(Text, nullable=False)
    starter_code = Column(Text, nullable=False)
    function_name = Column(String(80), nullable=False)
    test_cases = Column(Text, nullable=False)        # JSON string of test cases
    solution_approach = Column(Text, nullable=False) # Context for AI tutor
    edge_cases = Column(Text, nullable=True)         # JSON string of edge cases
    order_index = Column(Integer, default=0)
    is_preset = Column(Boolean, default=True)
    hints = Column(Text, nullable=True)              # JSON string: array of 3 hint strings

    attempts = relationship("Attempt", back_populates="problem", cascade="all, delete-orphan")

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(String(50), ForeignKey("problems.id"), nullable=False)
    code = Column(Text, nullable=False)
    status = Column(String(30), nullable=False)      # passed, wrong_answer, runtime_error, syntax_error
    error_type = Column(String(80), nullable=True)   # IndexError, TypeError, etc.
    error_message = Column(Text, nullable=True)
    error_line = Column(Integer, nullable=True)
    bug_category = Column(String(50), nullable=True) # indexing, loops, conditions, etc.
    passed_tests = Column(Integer, default=0)
    total_tests = Column(Integer, default=0)
    execution_time_ms = Column(Float, default=0.0)
    hints_used = Column(Integer, default=0)
    is_solved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    problem = relationship("Problem", back_populates="attempts")

class Weakness(Base):
    __tablename__ = "weaknesses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category = Column(String(50), unique=True, index=True, nullable=False) # e.g. "indexing"
    display_name = Column(String(80), nullable=False)
    mistake_count = Column(Integer, default=0)
    last_occurred = Column(DateTime, default=datetime.utcnow)

class TutorInteraction(Base):
    __tablename__ = "tutor_interactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(String(50), nullable=False)
    interaction_type = Column(String(30), nullable=False) # hint, explain_error, explain_concept, quality, edge_case
    hint_level = Column(Integer, nullable=True)           # 1, 2, 3
    student_code = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
