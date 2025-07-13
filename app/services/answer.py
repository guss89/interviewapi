from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
from typing import List, Dict

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

def get_avg_by_question(db: Session) -> List[Dict]:
    query = text("""
        SELECT 
            qe.description AS pregunta,
            (ROUND(SUM(ca.value) / (COUNT(*) * MAX_VALUES.max_value), 2) * 100) AS promedio_relativo
        FROM interview_questions AS iq
        INNER JOIN answers AS a ON iq.id = a.interview_question_id
        INNER JOIN cat_answer AS ca ON a.cat_answer_id = ca.id
        INNER JOIN questions AS qe ON qe.id = iq.question_id
        INNER JOIN (
            SELECT option_type, MAX(value) AS max_value
            FROM cat_answer
            GROUP BY option_type
        ) AS MAX_VALUES ON MAX_VALUES.option_type = ca.option_type
        GROUP BY qe.description, ca.option_type
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "pregunta": row[0],
            "promedio_relativo": float(row[1])
        }
        for row in rows
    ]