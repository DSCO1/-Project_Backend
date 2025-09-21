from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from ..core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    
    # --- ADD THESE NEW FIELDS ---
    current_education_level = Column(String, nullable=True) # e.g., "Class 12"
    stream = Column(String, nullable=True) # e.g., "Science"
    academic_marks = Column(Float, nullable=True) # e.g., 85.5 for percentage
    location = Column(String, nullable=True) # e.g., "Srinagar"

    quiz_answers = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())