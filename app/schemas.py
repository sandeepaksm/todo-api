from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# What user sends to CREATE a todo
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

# What user sends to UPDATE a todo
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# What API sends back as response
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
