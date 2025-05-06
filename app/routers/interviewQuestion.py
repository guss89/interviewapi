from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import routers, schemas, database, services

#Schemas
from app.schemas.interviewQuestion import InterviewQuestionOut, InterviewQuestionCreate, InterviewQuestionUpdate
#Services
from app.services.interviewQuestion import get_all_interviewQuestion, get_all_intervireQuestion_id, create_interviewQuestion, update_interviewQuestion, delete_interviewQuestion, get_interviews

router = APIRouter(prefix="/interviewQuestions", tags=["InterviewQuestions"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[InterviewQuestionOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_interviewQuestion(db)

@router.get("/{interview_id}", response_model=list[InterviewQuestionOut])
def list_all_by_id(interview_id:int ,db: Session = Depends(get_db)):
    return get_all_intervireQuestion_id(db = db,interview_id = interview_id )

@router.post("/", response_model=InterviewQuestionOut)
def create(InterviewQuestion: InterviewQuestionCreate, db:Session = Depends(get_db)):
    return create_interviewQuestion(db = db, interviewQuestion = InterviewQuestion)

@router.put("/{interview_id}", response_model=InterviewQuestionOut)
def update_endpoint(interviewQuestion_id:int, interviewQuestion:InterviewQuestionUpdate, db: Session = Depends(get_db)):
    update_intq = update_interviewQuestion(db = db, interviewQuestion_id = interviewQuestion_id, interviewQuestion_data = interviewQuestion)
    if not update_intq:
        raise HTTPException(status_code=404, detail="Interview Question not found")
    return update_intq

@router.delete("/{interview_id}")
def delete_endpoint(interviewQuestion_id:int, db:Session = Depends(get_db)):
    delete_iq = delete_interviewQuestion(db=db, interviewQuestion_id = interviewQuestion_id)
    if not delete_iq:
        raise HTTPException(status_code=404, detail="Interview not found")
    return delete_iq

@router.get("/get-interviews/{interview_id}",)
def get_main_interviews(interview_id:int,db: Session = Depends(get_db)):
    return get_interviews(db, interview_id = interview_id)