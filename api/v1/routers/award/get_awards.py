from fastapi import APIRouter

from api.services.award import AwardService


router = APIRouter(
    prefix="/get_awards"
)

@router.get('')
async def route():
    return await AwardService().get_all_awards()