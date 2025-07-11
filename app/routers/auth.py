from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, Token, UserCreate
from app.services.auth import login_user, create_user
from app import database



router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )
    return {"message": "Usuario creado correctamente"}