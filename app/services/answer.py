from sqlalchemy.orm import Session
from sqlalchemy import func, case

#schema
from app.schemas.answer import AnswerCreate, AnswerUpdate, AnswerOut

#Models
from app.models.answer import Answer
from app.models.waiter import Waiter
from app.models.catAnswer import CatAnswer

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

def get_rating_by_waiter(db:Session):
    ranking_query = (
        db.query(
            Waiter.name, Waiter.id,
            func.coalesce(func.avg(CatAnswer.value), 0.0).label("rating")
        )
        .outerjoin(Answer, Answer.waiter_id == Waiter.id)
        .outerjoin(CatAnswer, Answer.cat_answer_id == CatAnswer.id)
        .group_by(Waiter.id)
        .all()
    )

    return [{"id": id, "name": name, "ranking": float(rating)} for name, id, rating in ranking_query]

