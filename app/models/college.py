from sqlalchemy import Column, Integer, String, Text
from ..core.database import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    description = Column(Text, nullable=True)
    website_link = Column(String, nullable=True)