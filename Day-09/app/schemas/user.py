from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=20, description="required field")
    email: str = Field(..., min_length=2)


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[str] = None


class UserResponse(UserBase):
    id: UUID

    class Config:
        from_attributes = True
