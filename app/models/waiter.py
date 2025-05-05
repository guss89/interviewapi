from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Waiter(Base):
    __tablename__ = "waiters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)

     # Esto crea la relación con SQLAlchemy
    store = relationship("Store", back_populates="waiters")
    answers = relationship("Answer", back_populates="waiter")
