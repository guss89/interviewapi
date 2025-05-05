from sqlalchemy.orm import Session

#schema
from app.schemas.answer import AnswerCreate, AnswerUpdate, AnswerOut

#Models
from app.models.answer import Answer

def get_all_answer(db:Session):
    return db.query(Answer).all()

def get_all_by_waiter_id(db:Session, waiter_id:int):
    answers = db.query(Answer).filter(Answer.waiter_id == waiter_id).all()
    if answers:
        return answers
    else:
        return None
    
def create_answer(db:Session, answer: AnswerCreate):
    db_answer = Answer(**answer.dict())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer
