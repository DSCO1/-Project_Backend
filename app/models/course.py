from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .associations import college_course_association

from ..core.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    stream = Column(String)
    duration_years = Column(Integer)
    description = Column(Text, nullable=True)
    
    colleges = relationship("College", secondary=college_course_association, back_populates="courses")