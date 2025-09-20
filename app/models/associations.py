from sqlalchemy import Table, Column, Integer, ForeignKey
from ..core.database import Base

# This is not a model class, but a table definition for our many-to-many relationship
career_skill_association = Table('career_skills', Base.metadata,
    Column('career_id', Integer, ForeignKey('careers.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)