from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.fighter import FighterService
from db.database import get_db
from fastapi import Query

router = APIRouter(prefix="/get_fighters")

@router.get("")
async def get_all_fighters(
    db: AsyncSession = Depends(get_db),
    name: str = Query(None),
    municipality_id: int = Query(None)
):
    return await FighterService(db).get_all_fighters(name, municipality_id)