from sqlalchemy.orm import Session


#schema
from app.schemas.comments import CommentsCreate, CommentsUpdate, CommentsOut

#Models
from app.models.comments import Comments

def get_all_comments(db:Session):
    return db.query(Comments).all()

def create_comments(db:Session,comments: CommentsCreate):
    db_comment = Comments(**comments.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comments(db:Session, comment_id: int ,comment_data: CommentsUpdate ):
    db_comment = db.query(Comments).filter(Comments.id == comment_id).first()
    if not db_comment:
        return None
    
    for key, value in comment_data.dict(exclude_unset=True).items():
        setattr(db_comment, key, value)

    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comments(db:Session, comment_id:int):
    comment = db.query(Comments).filter(Comments.id == comment_id).first()
    if not comment:
        return None
    db.delete(comment)
    db.commit()
    return {"detail":"Comment deleted successfully"}