from uuid import uuid4, UUID
from models.user import fake_user
from schemas.user import UserCreate, UserUpdate


def create_user(user: UserCreate):
    user_id = uuid4()
    print(user_id)
    user_data = user.model_dump()
    fake_user[user_id] = user_data
    return {"id": user_id, **user_data}


def get_user(user_id: UUID):
    return fake_user.get(user_id)


def get_all_user():
    return [{"id": user_id, **data} for user_id, data in fake_user.items()]


def update_user(user_id: UUID, user: UserUpdate):
    stored_user = fake_user.get(user_id)
    if not stored_user:
        return None
    update_data = user.model_dump(exclude_unset=True)
    stored_user.update(update_data)
    return {"id": user_id, **stored_user}


def delete_user(user_id: UUID):
    user = fake_user.get(user_id)
    if not user:
        return None
    fake_user.pop(user_id, None)
    return {"message": "User deleted successfully"}
