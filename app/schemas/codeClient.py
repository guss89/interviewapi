from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class EstatusEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"
    pendiente = "pendiente"

class CodeClientBase(BaseModel):
    codeClient: str = Field(..., max_length=10)
    store_id: Optional[int]
    codeStatus: Optional[EstatusEnum] = EstatusEnum.activo

class CodeClientCreate(CodeClientBase):
    store_id: int

class CodeClientUpdate(CodeClientBase):
    pass

class CodeClientOut(CodeClientBase):
    id: int

    class Config:
        from_attributes = True 