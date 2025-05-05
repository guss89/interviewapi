from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

#Schemas
from app.schemas.interview import InterviewOut, InterviewCreate, InterviewUpdate
#Services
from app.services.interview import get_all_interview, create_interview, update_interview, delete_interview

router = APIRouter(prefix="/interviews", tags=["Interviews"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[InterviewOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_interview(db)

@router.post("/", response_model=InterviewOut)
def create(Interview: InterviewCreate, db:Session = Depends(get_db)):
    return create_interview(db = db, interview = Interview)

@router.put("/{interview_id}", response_model=InterviewOut)
def update_endpoint(interview_id:int, interview:InterviewUpdate, db: Session = Depends(get_db)):
    update_itr = update_interview(db = db, interview_id = interview_id, interview_data = interview)
    if not update_itr:
        raise HTTPException(status_code=404, detail="Interview not found")
    return update_itr

@router.delete("/{interview_id}")
def delete_endpoint(interview_id:int, db:Session = Depends(get_db)):
    delete_str = delete_interview(db=db, interview_id = interview_id)
    if not delete_str:
        raise HTTPException(status_code=404, detail="Interview not found")
    return delete_str