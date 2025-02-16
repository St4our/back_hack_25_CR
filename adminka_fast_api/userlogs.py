from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from adminka_fast_api.services.user_logs import UserLogService
from adminka_fast_api import logger  # Импорт логгера

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
    logger.info(f"Запрос: Получение user log ID {log_id}")
    result = await user_log_service.get_log(log_id)

    if "log" not in result:
        logger.warning(f"User log ID {log_id} не найден")
        raise HTTPException(status_code=404, detail="Log not found")

    logger.info(f"Ответ: {result['log']}")
    return result["log"]


@router.get("/", response_model=List[UserLogResponseSchema])
async def get_all_user_logs():
    """
    Получить все логи пользователей
    """
    logger.info("Запрос: Получение всех user logs")
    result = await user_log_service.get_all_logs()
    logger.info(f"Найдено user logs: {len(result['logs'])}")
    return result["logs"]


@router.post("/", response_model=dict)
async def create_user_log(log_data: UserLogCreateSchema):
    """
    Создать новый лог пользователя
    """
    logger.info(f"Запрос: Создание user log - {log_data.dict()}")
    result = await user_log_service.create(**log_data.dict())
    logger.info(f"User log создан: {result}")
    return result


@router.delete("/{log_id}", response_model=dict)
async def delete_user_log(log_id: int):
    """
    Удалить лог пользователя
    """
    logger.info(f"Запрос: Удаление user log ID {log_id}")
    result = await user_log_service.delete(log_id)
    logger.info(f"User log удален: {result}")
    return result
