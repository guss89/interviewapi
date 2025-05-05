from sqlalchemy.orm import Session

#Schemas
from app.schemas.waiter  import WaiterCreate, WaiterUpdate

#Models
from app.models.waiter import Waiter

def get_all_waiters(db:Session):
    return db.query(Waiter).all()

def create_waiter(db:Session,waiter: WaiterCreate):
    db_waiter = Waiter(**waiter.dict())
    db.add(db_waiter)
    db.commit()
    db.refresh(db_waiter)
    return db_waiter

def update_waiter(db:Waiter, waiter_id: int ,waiter_data: WaiterUpdate ):
    db_waiter = db.query(Waiter).filter(Waiter.id == waiter_id).first()
    if not db_waiter:
        return None
    
    for key, value in waiter_data.dict(exclude_unset=True).items():
        setattr(db_waiter, key, value)

    db.commit()
    db.refresh(db_waiter)
    return db_waiter

def delete_waiter(db:Session, waiter_id:int):
    waiter = db.query(Waiter).filter(Waiter.id == waiter_id).first()
    if not waiter:
        return None
    db.delete(waiter)
    db.commit()
    return {"detail":"Waiter deleted successfully"}