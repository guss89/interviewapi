from sqlalchemy.orm import Session

#Schemas
from app.schemas.hostess  import HostessCreate, HostessUpdate

#Models
from app.models.hostess import Hostess

def get_all_hostess(db:Session):
    return db.query(Hostess).all()

def create_hostess(db:Session,hostess: HostessCreate):
    db_hostess = Hostess(**hostess.dict())
    db.add(db_hostess)
    db.commit()
    db.refresh(db_hostess)
    return db_hostess

def update_hostess(db:Hostess, hostess_id: int, hostess_data: HostessUpdate):
    db_hostess = db.query(Hostess).filter(Hostess.id == hostess_id).first()
    if not db_hostess:
        return None
    
    for key, value in hostess_data.dict(exclude_unset=True).items():
        setattr(db_hostess, key, value)

    db.commit()
    db.refresh(db_hostess)
    return db_hostess

def delete_hostess(db:Session, hostess_id:int):
    hostess = db.query(Hostess).filter(Hostess.id == hostess_id).first()
    if not hostess:
        return None
    db.delete(hostess)
    db.commit()
    return {"detail":"Hostess deleted successfully"}