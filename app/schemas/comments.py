from pydantic import BaseModel, Field
from typing import Optional

class CommentsBase(BaseModel):
    description: str = Field(..., max_length=255)
    client_id: Optional[int] = None

class CommentsCreate(CommentsBase):
    pass

class CommentsUpdate(CommentsBase):
    pass

class CommentsOut(CommentsBase):
    id: int

    class Config:
        from_attributes = True 
        client_id: Optional[int] = None