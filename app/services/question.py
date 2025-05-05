from sqlalchemy.orm import Session

#Models
from app.models.question import Question

#schema
from app.schemas.question import QuestionCreate, QuestionUpdate, QuestionOut

def get_all_questions(db:Session):
    return db.query(Question).all()

def create_question(db:Session,question: QuestionCreate):
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def update_question(db:Session, question_id: int ,question_data: QuestionUpdate ):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        return None
    
    for key, value in question_data.dict(exclude_unset=True).items():
        setattr(db_question, key, value)

    db.commit()
    db.refresh(db_question)
    return db_question

def delete_question(db:Session, question_id:int):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        return None
    db.delete(question)
    db.commit()
    return {"detail":"Question deleted successfully"}