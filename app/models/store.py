from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    image = Column(String(255), nullable=True)


    # Relación inversa
    waiters = relationship("Waiter", back_populates="store")
    interviews = relationship("Interview", back_populates="store")