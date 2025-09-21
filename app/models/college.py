from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .associations import college_course_association

from ..core.database import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    description = Column(Text, nullable=True)
    website_link = Column(String, nullable=True)
    
    courses = relationship("Course", secondary=college_course_association, back_populates="colleges")