from sqlalchemy.orm import Session

#schema
from app.schemas.store import StoreCreate, StoreUpdate

#Models
from app.models.store import Store

def get_all_stores(db:Session):
    return db.query(Store).all()

def create_store(db:Session,store: StoreCreate):
    db_store = Store(**store.dict())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def update_store(db:Session, store_id: int ,store_data: StoreUpdate ):
    db_store = db.query(Store).filter(Store.id == store_id).first()
    if not db_store:
        return None
    
    for key, value in store_data.dict(exclude_unset=True).items():
        setattr(db_store, key, value)

    db.commit()
    db.refresh(db_store)
    return db_store

def delete_store(db:Session, store_id:int):
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        return None
    db.delete(store)
    db.commit()
    return {"detail":"Store deleted successfully"}