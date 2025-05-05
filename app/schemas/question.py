from pydantic import BaseModel, Field
from typing import Optional


class QuestionBase(BaseModel):
    description: Optional[str] = Field(None, max_length=255)

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int

    class Config:
        from_attributes = True 