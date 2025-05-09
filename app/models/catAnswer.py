from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class CatAnswer(Base):
    __tablename__ = "cat_answer"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    value = Column(Integer, default=0)
    option_type = Column(String (25), nullable=False)
    emoji = Column(String(255), nullable=True)