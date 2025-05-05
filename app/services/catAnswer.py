from sqlalchemy.orm import Session


#schema
from app.schemas.catAnswer import CatAnswerCreate, CatAnswerUpdate, CatAnswerOut

#Models
from app.models.catAnswer import CatAnswer

def get_all_catAnswer(db:Session):
    return db.query(CatAnswer).all()

def create_catAnswer(db:Session,catAnswer: CatAnswerCreate):
    db_catAnswer = CatAnswer(**catAnswer.dict())
    db.add(db_catAnswer)
    db.commit()
    db.refresh(db_catAnswer)
    return db_catAnswer

def update_catAnswer(db:Session, catAnswer_id: int ,catAnswer_data: CatAnswerUpdate ):
    db_catAnswer = db.query(CatAnswer).filter(CatAnswer.id == catAnswer_id).first()
    if not db_catAnswer:
        return None
    
    for key, value in catAnswer_data.dict(exclude_unset=True).items():
        setattr(db_catAnswer, key, value)

    db.commit()
    db.refresh(db_catAnswer)
    return db_catAnswer

def delete_catAnswer(db:Session, catAnswer_id:int):
    catAnswer = db.query(CatAnswer).filter(CatAnswer.id == catAnswer_id).first()
    if not catAnswer:
        return None
    db.delete(catAnswer)
    db.commit()
    return {"detail":"Answer deleted successfully"}