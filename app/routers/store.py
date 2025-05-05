from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import routers, schemas, database, services

#Schemas
from app.schemas.store import StoreOut, StoreUpdate, StoreCreate
#Services
from app.services.store import get_all_stores, create_store, update_store, delete_store

router = APIRouter(prefix="/stores", tags=["Stores"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[StoreOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_stores(db)

@router.post("/", response_model=StoreOut)
def create(Store: StoreCreate, db:Session = Depends(get_db)):
    return create_store(db = db, store = Store)

@router.put("/{store_id}", response_model=StoreOut)
def update_endpoint(store_id:int, store:StoreUpdate, db: Session = Depends(get_db)):
    update_str = update_store(db = db, store_id = store_id, store_data = store)
    if not update_str:
        raise HTTPException(status_code=404, detail="Store not found")
    return update_str

@router.delete("/{store_id}")
def delete_endpoint(store_id:int, db:Session = Depends(get_db)):
    delete_str = delete_store(db=db, store_id = store_id)
    if not delete_str:
        raise HTTPException(status_code=404, detail="Store not found")
    return delete_str