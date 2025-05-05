from sqlalchemy.orm import Session
from fastapi import HTTPException

#schema
from app.schemas.interview import InterviewCreate, InterviewUpdate, InterviewOut

#Models
from app.models.interview import Interview

def get_all_interview(db:Session):
    try:
        return db.query(Interview).all()
    except Exception as e:
        HTTPException(status_code=500, detail=str(e))
    

def create_interview(db:Session,interview: InterviewCreate):
    db_interview = Interview(**interview.dict())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

def update_interview(db:Session, interview_id: int ,interview_data: InterviewUpdate ):
    db_interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not db_interview:
        return None
    
    for key, value in interview_data.dict(exclude_unset=True).items():
        setattr(db_interview, key, value)

    db.commit()
    db.refresh(db_interview)
    return db_interview

def delete_interview(db:Session, interview_id:int):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        return None
    db.delete(interview)
    db.commit()
    return {"detail":"Interview deleted successfully"}