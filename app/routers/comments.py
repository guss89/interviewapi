from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

#Schemas
from app.schemas.comments import CommentsOut, CommentsCreate, CommentsUpdate
#Services
from app.services.comments import get_all_comments, create_comments, update_comments, delete_comments

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CommentsOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_comments(db)

@router.post("/", response_model=CommentsOut)
def create(Comments: CommentsCreate, db:Session = Depends(get_db)):
    return create_comments(db = db, comments = Comments)

@router.put("/{comment_id}", response_model=CommentsOut)
def update_endpoint(comment_id:int, comment:CommentsUpdate, db: Session = Depends(get_db)):
    update_cmt = update_comments(db = db, comment_id = comment_id, comment_data = comment)
    if not update_cmt:
        raise HTTPException(status_code=404, detail="Comment not found")
    return update_cmt

@router.delete("/{comment_id}")
def delete_endpoint(comment_id:int, db:Session = Depends(get_db)):
    delete_cmt = delete_comments(db=db, comment_id = comment_id)
    if not delete_cmt:
        raise HTTPException(status_code=404, detail="Comment not found")
    return delete_cmt