from typing import Optional
from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str = Field(..., max_length=60)
    done: bool = False
    
class Todo(TodoBase):
    id: int
    
    class Config:
        from_attributes = True
        
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=60)
    done: Optional[bool] = False