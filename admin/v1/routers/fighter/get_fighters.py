from fastapi import APIRouter

from api.services.fighter import FighterService


router = APIRouter(
    prefix="/get_fighters"
)

@router.get('')
async def route():
    return await FighterService().get_all_fighters()