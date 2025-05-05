from pydantic import BaseModel, Field
from typing import Optional


class StoreBase(BaseModel):
    name: str = Field(..., max_length=100)
    image: Optional[str] = Field(None, max_length=255)

class StoreCreate(StoreBase):
    pass

class StoreUpdate(StoreBase):
    pass

class StoreOut(StoreBase):
    id: int

    class Config:
        from_attributes = True 