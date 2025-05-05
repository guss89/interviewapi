from pydantic import BaseModel, Field
from typing import Optional

class HostessBase(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=10)

class HostessCreate(HostessBase):
    pass

class HostessUpdate(HostessBase):
    pass

class HostessOut(HostessBase):
    id: int

    class Config:
        from_attributes = True 