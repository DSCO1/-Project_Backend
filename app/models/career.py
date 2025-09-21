from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .associations import career_skill_association

from ..core.database import Base

class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    avg_salary = Column(String, nullable=True)
    source = Column(String, default="curated")
    
    skills = relationship("Skill", secondary=career_skill_association, back_populates="careers")