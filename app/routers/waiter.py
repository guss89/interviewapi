from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

#Schemas
from app.schemas.waiter import WaiterOut, WaiterCreate, WaiterUpdate
#Services
from app.services.waiter import get_all_waiters, create_waiter, update_waiter, delete_waiter

router = APIRouter(prefix="/waiters", tags=["Waiters"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[WaiterOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_waiters(db)

@router.post("/", response_model=WaiterOut)
def create(Waiter: WaiterCreate, db:Session = Depends(get_db)):
    return create_waiter(db = db, waiter = Waiter)

@router.put("/{waiter_id}", response_model=WaiterOut)
def update_endpoint(waiter_id:int, waiter:WaiterUpdate, db: Session = Depends(get_db)):
    update_wtr = update_waiter(db = db, waiter_id = waiter_id, waiter_data = waiter)
    if not update_wtr:
        raise HTTPException(status_code=404, detail="Waiter not found")
    return update_wtr

@router.delete("/{waiter_id}")
def delete_endpoint(waiter_id:int, db:Session = Depends(get_db)):
    delete_wtr = delete_waiter(db=db, waiter_id = waiter_id)
    if not delete_wtr:
        raise HTTPException(status_code=404, detail="Store not found")
    return delete_wtr