from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

#Schemas
from app.schemas.hostess import HostessOut, HostessCreate, HostessUpdate
#Services
from app.services.hostess import get_all_hostess, create_hostess, update_hostess, delete_hostess 


router = APIRouter(prefix="/hostess", tags=["Hostess"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[HostessOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_hostess(db)

@router.post("/", response_model=HostessOut)
def create(Hostess: HostessCreate, db:Session = Depends(get_db)):
    return create_hostess(db = db, hostess = Hostess)

@router.put("/{hostess_id}", response_model=HostessOut)
def update_endpoint(hostess_id:int, hostess:HostessUpdate, db: Session = Depends(get_db)):
    update_hos = update_hostess(db = db, hostess_id = hostess_id, waiter_data = hostess)
    if not update_hos:
        raise HTTPException(status_code=404, detail="Hostess not found")
    return update_hos

@router.delete("/{hostess_id}")
def delete_endpoint(hostess_id:int, db:Session = Depends(get_db)):
    delete_hos = delete_hostess(db=db, hostess_id = hostess_id)
    if not delete_hos:
        raise HTTPException(status_code=404, detail="Hostess not found")
    return delete_hos