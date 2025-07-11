from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=True) 
    
    client = relationship("Client")