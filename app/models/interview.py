from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)


    # Esto crea la relación con SQLAlchemy
    store = relationship("Store", back_populates="interviews")
    questions = relationship("InterviewQuestion", back_populates="interview")