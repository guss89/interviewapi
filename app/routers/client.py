from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

#Schemas
from app.schemas.client import ClientOut, ClientCreate, ClientUpdate
#Services
from app.services.client import get_all_client, create_client, update_client, delete_client

router = APIRouter(prefix="/clients", tags=["Clients"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ClientOut])
def list_all(db: Session = Depends(get_db)):
    return get_all_client(db)

@router.post("/", response_model=ClientOut)
def create(Client: ClientCreate, db:Session = Depends(get_db)):
    return create_client(db = db, client = Client)

@router.put("/{client_id}", response_model=ClientOut)
def update_endpoint(client_id:int, client:ClientUpdate, db: Session = Depends(get_db)):
    update_clt = update_client(db = db, client_id = client_id, client_data = client)
    if not update_clt:
        raise HTTPException(status_code=404, detail="Waiter not found")
    return update_clt

@router.delete("/{client_id}")
def delete_endpoint(client_id:int, db:Session = Depends(get_db)):
    delete_clt = delete_client(db=db, client_id = client_id)
    if not delete_clt:
        raise HTTPException(status_code=404, detail="Client not found")
    return delete_clt