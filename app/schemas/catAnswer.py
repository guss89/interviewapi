from pydantic import BaseModel, Field
from typing import Optional


class CatAnswerBase(BaseModel):
    description: str = Field(..., max_length=255)
    value: int

class CatAnswerCreate(CatAnswerBase):
    pass

class CatAnswerUpdate(CatAnswerBase):
    pass

class CatAnswerOut(CatAnswerBase):
    id: int

    class Config:
        from_attributes = True 