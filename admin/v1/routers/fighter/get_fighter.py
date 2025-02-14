from fastapi import APIRouter

from api.services.fighter import FighterService

router = APIRouter(
    prefix="/get_fighter"
)

@router.get('')
async def route(
    id: int
):
    return await FighterService().get_chat(
        id=id
    )