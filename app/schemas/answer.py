from pydantic import BaseModel, Field
from typing import Optional

class AnswerBase(BaseModel):
    cat_answer_id: int = Field(..., description="ID Anwer")
    interview_question_id: int = Field(..., description="ID Interview")
    waiter_id: int = Field(..., description="ID Waiter")
    hostess_id: int = Field(..., description="ID Hostess")

class AnswerCreate(AnswerBase):
    cat_answer_id: int
    interview_question_id: int
    waiter_id: int
    hostess_id: int

class AnswerUpdate(AnswerBase):
    pass

class AnswerOut(AnswerBase):
    id: int

    class Config:
        from_attributes = True 