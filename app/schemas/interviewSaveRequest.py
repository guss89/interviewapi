from pydantic import BaseModel
from typing import List

class AnswerSchema(BaseModel):
    interview_question_id: int
    cat_answer_id: int

class ClientSchema(BaseModel):
    name: str
    phone: int

class InterviewRequest(BaseModel):
    waiter: int
    store_id: int
    interview_id: int
    hostess: int
    answers: List[AnswerSchema]
    comments: str
    client: ClientSchema