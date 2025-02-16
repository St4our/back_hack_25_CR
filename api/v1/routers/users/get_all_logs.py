from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_logs import UserLogService
from db.database import get_db

router = APIRouter(prefix="/get_all_logs")

@router.get("")
async def get_all_logs(
    db: AsyncSession = Depends(get_db),
    user_name: str = Query(None),
    fighter_id: int = Query(None),
):
    """
    Получение всех логов с фильтрацией по user_name или fighter_id
    """
    return await UserLogService(db).get_all_logs(user_name, fighter_id)