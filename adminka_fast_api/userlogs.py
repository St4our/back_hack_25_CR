from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from api.services.user_logs import UserLogService

router = APIRouter(
    prefix="/user_logs",
    tags=["user_logs"]
)

user_log_service = UserLogService()


class UserLogCreateSchema(BaseModel):
    user_id: int
    fighter_id: int
    name: str
    birth_death_years: str
    municipality_id: Optional[int] = None
    short_info: Optional[str] = None
    photo_path: Optional[str] = None


class UserLogResponseSchema(BaseModel):
    id: int
    user_id: int
    fighter_id: int
    name: str
    birth_death_years: str
    municipality_id: Optional[int]
    short_info: Optional[str]
    photo_path: Optional[str]


@router.get("/{log_id}", response_model=UserLogResponseSchema)
async def get_user_log(log_id: int):
    """
    Получить лог по ID
    """
    result = await user_log_service.get_log(log_id)
    if "log" not in result:
        raise HTTPException(status_code=404, detail="Log not found")
    return result["log"]


@router.get("/", response_model=List[UserLogResponseSchema])
async def get_all_user_logs():
    """
    Получить все логи пользователей
    """
    result = await user_log_service.get_all_logs()
    return result["logs"]


@router.post("/", response_model=dict)
async def create_user_log(log_data: UserLogCreateSchema):
    """
    Создать новый лог пользователя
    """
    result = await user_log_service.create(**log_data.dict())
    return result


@router.delete("/{log_id}", response_model=dict)
async def delete_user_log(log_id: int):
    """
    Удалить лог пользователя
    """
    result = await user_log_service.delete(log_id)
    return result
