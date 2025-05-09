from sqlalchemy.orm import Session


#schema
from app.schemas.client import ClientCreate, ClientUpdate, ClientOut

#Models
from app.models.client import Client

def get_all_client(db:Session):
    return db.query(Client).all()

def create_client(db:Session,client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db:Session, client_id: int ,client_data: ClientUpdate ):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if not db_client:
        return None
    
    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(db_client, key, value)

    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db:Session, client_id:int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        return None
    db.delete(client)
    db.commit()
    return {"detail":"Client deleted successfully"}