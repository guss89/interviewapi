from pydantic import BaseModel, Field
from typing import Optional

class InterviewQuestionBase(BaseModel):
    question_id: int = Field(..., description="ID Question")
    interview_id: int = Field(..., description="ID Interview")
    store_id: int = Field(..., description="ID Store")

class InterviewQuestionCreate(InterviewQuestionBase):
    interview_id: int

class InterviewQuestionUpdate(InterviewQuestionBase):
    interview_id: Optional[int]
    store_id: Optional[int]
    question_id: Optional[int]

class InterviewQuestionOut(InterviewQuestionBase):
    id: int

    class Config:
        from_attributes = True 