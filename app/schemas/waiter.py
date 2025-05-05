from pydantic import BaseModel, Field
from typing import Optional

class WaiterBase(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=10)
    store_id: Optional[int]

class WaiterCreate(WaiterBase):
    store_id: int

class WaiterUpdate(WaiterBase):
    pass

class WaiterOut(WaiterBase):
    id: int

    class Config:
        from_attributes = True 