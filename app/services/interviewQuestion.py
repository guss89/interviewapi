from sqlalchemy.orm import Session
from sqlalchemy import join, select

#schema
from app.schemas.interviewQuestion import InterviewQuestionUpdate, InterviewQuestionCreate, InterviewQuestionOut

#Models
from app.models.interviewQuestion import InterviewQuestion
from app.models.store import Store
from app.models.interview import Interview
from app.models.question import Question
from app.models.catAnswer import CatAnswer

def get_all_interviewQuestion(db:Session):
    return db.query(InterviewQuestion).all()

def get_all_intervireQuestion_id(db:Session, interview_id: int):
    interviews = db.query(InterviewQuestion).filter(InterviewQuestion.interview_id == interview_id).all()
    if interviews:
       return interviews
    else:
        return None
    
def create_interviewQuestion(db:Session, interviewQuestion: InterviewQuestionCreate):
    db_interview = InterviewQuestion(**interviewQuestion.dict())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

def update_interviewQuestion(db:Session, interviewQuestion_id: int ,interviewQuestion_data: InterviewQuestionUpdate ):
    db_interviewQuestion = db.query(InterviewQuestion).filter(InterviewQuestion.id == interviewQuestion_id).first()
    if not db_interviewQuestion:
        return None
    
    for key, value in interviewQuestion_data.dict(exclude_unset=True).items():
        setattr(db_interviewQuestion, key, value)

    db.commit()
    db.refresh(db_interviewQuestion)
    return db_interviewQuestion

def delete_interviewQuestion(db:Session, interviewQuestion_id:int):
    interview = db.query(InterviewQuestion).filter(InterviewQuestion.id == interviewQuestion_id).first()
    if not interview:
        return None
    db.delete(interview)
    db.commit()
    return {"detail":"Interview deleted successfully"}


def get_interviews(db:Session, interview_id: int)->list[dict]:
    query = db.query(
        InterviewQuestion.id,
        Store.name.label("store"),
        Interview.name.label("interview"),
        Question.description.label("question")
    ).join(Store, InterviewQuestion.store) \
     .join(Interview, InterviewQuestion.interview) \
     .join(Question, InterviewQuestion.question)\
     .filter(InterviewQuestion.interview_id == interview_id)
    
    store = db.query(Store.name.label("store")).join(Store, InterviewQuestion.store).filter(InterviewQuestion.interview_id == interview_id).first()
    interview = db.query(Interview.name.label("interview")).join(Interview, InterviewQuestion.interview).filter(InterviewQuestion.interview_id == interview_id).first()

    queryOptions = db.query(CatAnswer).all()
    catOptions = [{"id":option.id, "description":option.description, "value":option.value} for option in queryOptions]
    rows = db.execute(query).all()
    questions = [
        {
            "id": row.id,
            "question": row.question,
            "options": catOptions
        }
        for row in rows
    ]
    return {
        "store":store.store,
        "interview": interview.interview,
        "questions": questions
    }