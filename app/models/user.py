from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from ..core.database import Base

class User(Base):
    __tablename__ = "users"

    # We use the Firebase UID as our primary key. It's a string.
    id = Column(String, primary_key=True, index=True)
    
    # We can store the user's name for personalization.
    name = Column(String, nullable=True)

    # We use a JSONB field to flexibly store the quiz answers.
    quiz_answers = Column(JSONB, nullable=True)
    
    # It's good practice to timestamp when the record was created.
    created_at = Column(DateTime(timezone=True), server_default=func.now())