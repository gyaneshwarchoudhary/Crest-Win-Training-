from uuid import UUID
from typing import List
from fastapi import APIRouter, HTTPException


from schemas.user import UserCreate, UserUpdate, UserResponse

from services import user as User

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
def get_users():
    return User.get_all_user()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID):
    user = User.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return {"id": user_id, **user}


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return User.create_user(user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: UUID, user: UserUpdate):
    update_user = User.update_user(user_id, user)
    if not update_user:
        raise HTTPException(status_code=404, detail="user not found")
    return update_user


@router.delete("/{user_id}")
def delete_user(user_id: UUID):
    deleted_user = User.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="user not found")
    return deleted_user
