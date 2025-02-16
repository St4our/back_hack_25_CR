from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_logs import UserLogService
from db.database import get_db

router = APIRouter(prefix="/get_log")

@router.get("")
async def get_log_by_id(log_id: int, db: AsyncSession = Depends(get_db)):
    """
    Получение лога по ID с user_name вместо user_id
    """
    log = await UserLogService(db).get_log(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return log