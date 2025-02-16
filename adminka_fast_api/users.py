from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from typing import List
from pydantic import BaseModel, EmailStr

from adminka_fast_api.services.user import UserService
from db.models.users import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

user_service = UserService()


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    is_admin: bool


@router.post("/", response_model=UserResponseSchema)
async def create_user(user_data: UserCreateSchema, bg_tasks: BackgroundTasks):
    """
    Создать нового пользователя
    """
    result = await user_service.create(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,
        bg_tasks=bg_tasks
    )
    if isinstance(result, HTTPException):
        raise result
    return result


@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(user_id: int):
    """
    Получить пользователя по ID
    """
    user = await user_service.get(None, id=user_id)
    if "user" not in user:
        raise HTTPException(status_code=404, detail="User not found")
    return user["user"]


@router.get("/", response_model=List[UserResponseSchema])
async def get_all_users():
    """
    Получить всех пользователей
    """
    users = await user_service.get_all()
    return users


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    """
    Удалить пользователя
    """
    result = await user_service.delete(user_id)
    return result
