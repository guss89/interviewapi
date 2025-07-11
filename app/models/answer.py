from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    interview_question_id = Column(Integer, ForeignKey("interview_questions.id"))
    waiter_id = Column(Integer, ForeignKey("waiters.id", ondelete="CASCADE"), nullable=False)
    cat_answer_id = Column(Integer, ForeignKey("cat_answer.id"), nullable=False)
    hostess_id = Column(Integer, ForeignKey("hostess.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=True) 

        # Esto crea la relación con SQLAlchemy
    interview_question = relationship("InterviewQuestion")
    option = relationship("CatAnswer")
    hostess = relationship("Hostess")
    waiter = relationship("Waiter", back_populates="answers", passive_deletes=True)
    client = relationship("Client") 