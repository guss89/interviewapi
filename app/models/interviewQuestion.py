from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    id = Column(Integer, primary_key=True, index=True)
    interview_id = Column(Integer, ForeignKey("interviews.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)

    interview = relationship("Interview", back_populates="questions")
    question = relationship("Question")  
    store = relationship("Store")  