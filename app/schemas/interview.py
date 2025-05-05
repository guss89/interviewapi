from pydantic import BaseModel, Field
from typing import Optional


class InterviewBase(BaseModel):
    name: str = Field(..., max_length=100)
    store_id: Optional[int]

class InterviewCreate(InterviewBase):
    store_id: int

class InterviewUpdate(InterviewBase):
    pass

class InterviewOut(InterviewBase):
    id: int

    class Config:
        from_attributes = True 