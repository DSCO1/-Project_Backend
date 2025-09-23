from sqlalchemy import Table, Column, Integer, ForeignKey
from ..core.database import Base

# Links careers to skills
career_skill_association = Table('career_skills', Base.metadata,
    Column('career_id', Integer, ForeignKey('careers.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

# Links careers to courses
career_course_association = Table('career_courses', Base.metadata,
    Column('career_id', Integer, ForeignKey('careers.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Links colleges to courses
college_course_association = Table('college_courses', Base.metadata,
    Column('college_id', Integer, ForeignKey('colleges.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)