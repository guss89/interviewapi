from pydantic import BaseModel, Field
from typing import Optional

class ClientBase(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=25)

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int

    class Config:
        from_attributes = True 