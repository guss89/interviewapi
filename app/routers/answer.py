from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import routers, schemas, database, services

#Schemas
from app.schemas.answer import AnswerCreate, AnswerUpdate, AnswerOut
#Services
from app.services.answer import get_all_answer, get_all_by_waiter_id, create_answer

router = APIRouter(prefix="/answers", tags=["Answers"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AnswerOut])
def list_all(db:Session = Depends(get_db)):
    return get_all_answer(db)

@router.get("/{waiter_id}", response_model=list[AnswerOut])
def list_all_by_waiter(waiter_id:int, db:Session = Depends(get_db)):
    return get_all_by_waiter_id(db = db, waiter_id = waiter_id)

@router.post("/", response_model=AnswerOut)
def create(Answer: AnswerCreate, db:Session = Depends(get_db)):
    return create_answer(db = db, answer = Answer)