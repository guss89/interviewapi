from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database

#Schemas
from app.schemas.question import QuestionOut, QuestionCreate, QuestionUpdate
#Services
from app.services.question import get_all_questions, create_question, update_question, delete_question

router = APIRouter(prefix="/questions", tags=["Questions"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[QuestionOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_questions(db)

@router.post("/", response_model=QuestionOut)
def create(Question: QuestionCreate, db:Session = Depends(get_db)):
    return create_question(db = db, question = Question)

@router.put("/{question_id}", response_model=QuestionOut)
def update_endpoint(question_id:int, question:QuestionUpdate, db: Session = Depends(get_db)):
    update_qst = update_question(db = db, question_id = question_id, question_data = question)
    if not update_qst:
        raise HTTPException(status_code=404, detail="Question not found")
    return update_qst

@router.delete("/{question_id}")
def delete_endpoint(question_id:int, db:Session = Depends(get_db)):
    delete_qst = delete_question(db=db, question_id = question_id)
    if not delete_qst:
        raise HTTPException(status_code=404, detail="Store not found")
    return delete_qst