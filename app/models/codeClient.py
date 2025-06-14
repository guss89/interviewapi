from enum import Enum
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Enum as SQLEnum

class EstatusEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"
    pendiente = "pendiente"

class CodeClient(Base):
    __tablename__ = "codeClients"

    id = Column(Integer, primary_key=True, index=True)
    codeClient = Column(String(10), nullable=False)
    codeStatus = Column(SQLEnum(EstatusEnum), nullable=False, default=EstatusEnum.activo) 
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    client = relationship("Client") 