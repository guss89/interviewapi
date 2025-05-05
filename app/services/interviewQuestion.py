from sqlalchemy.orm import Session

#schema
from app.schemas.interviewQuestion import InterviewQuestionUpdate, InterviewQuestionCreate, InterviewQuestionOut

#Models
from app.models.interviewQuestion import InterviewQuestion

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