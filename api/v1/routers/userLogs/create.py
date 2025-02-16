from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_logs import UserLogService
from db.database import get_db
from db.models import User
from api.utils import get_current_user
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/create")

class UserLogCreateSchema(BaseModel):
    fighter_id: int
    name: str
    birth_death_years: str
    municipality_id: Optional[int] = None
    short_info: Optional[str] = None
    photo_path: Optional[str] = None

@router.post("")
async def create_log(
    log_data: UserLogCreateSchema,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Создание лога пользователя
    """
    return await UserLogService(db).create(
        user_id=user.id,
        fighter_id=log_data.fighter_id,
        name=log_data.name,
        birth_death_years=log_data.birth_death_years,
        municipality_id=log_data.municipality_id,
        short_info=log_data.short_info,
        photo_path=log_data.photo_path
    )