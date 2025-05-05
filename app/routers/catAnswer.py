from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database

#Schemas
from app.schemas.catAnswer import CatAnswerOut, CatAnswerCreate, CatAnswerUpdate
#Services
from app.services.catAnswer import get_all_catAnswer, create_catAnswer, update_catAnswer, delete_catAnswer

router = APIRouter(prefix="/cat-answers", tags=["CatAnswers"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CatAnswerOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_catAnswer(db)

@router.post("/", response_model=CatAnswerOut)
def create(CatAnswer: CatAnswerCreate, db:Session = Depends(get_db)):
    return create_catAnswer(db = db, catAnswer = CatAnswer)

@router.put("/{catAnswer_id}", response_model=CatAnswerOut)
def update_endpoint(catAnswer_id:int, catAnswer:CatAnswerUpdate, db: Session = Depends(get_db)):
    update_cat = update_catAnswer(db = db, catAnswer_id = catAnswer_id, catAnswer_data = catAnswer)
    if not update_cat:
        raise HTTPException(status_code=404, detail="Answer not found")
    return update_cat

@router.delete("/{catAnswer_id}")
def delete_endpoint(catAnswer_id:int, db:Session = Depends(get_db)):
    delete_cat = delete_catAnswer(db=db, catAnswer_id = catAnswer_id)
    if not delete_cat:
        raise HTTPException(status_code=404, detail="Answer not found")
    return delete_cat