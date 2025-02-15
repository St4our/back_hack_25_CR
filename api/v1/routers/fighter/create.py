from fastapi import APIRouter, Depends
from api.services.fighter import FighterService
from db.models import User
from api.utils import get_current_user
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/fighters")

class FighterCreateSchema(BaseModel):
    name: str
    birth_death_years: str
    municipality_id: int
    short_info: Optional[str] = None
    photo_path: Optional[str] = None


@router.post("/create")
async def create_fighter(
    name: str, 
    birth_death_years: str, 
    municipality_id: int, 
    short_info: str, 
    photo_path: str, 
    user: User = Depends(get_current_user)
):
    """
    Создает нового бойца и записывает событие в user_logs
    """
    return await FighterService().create(
        user_id=user.id,
        name=name,
        birth_death_years=birth_death_years,
        municipality_id=municipality_id,
        short_info=short_info,
        photo_path=photo_path
    )