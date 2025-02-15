from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.fighter import FighterService
from db.database import get_db

router = APIRouter(prefix="/get_fighter")

@router.get("")
async def get_fighter(id: int, db: AsyncSession = Depends(get_db)):
    return await FighterService(db).get_fighter(id=id)
