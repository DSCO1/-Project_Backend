from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .associations import career_skill_association

from ..core.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    careers = relationship("Career", secondary=career_skill_association, back_populates="skills")