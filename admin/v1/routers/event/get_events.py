from fastapi import APIRouter

from api.services.events import  EventService

router = APIRouter(
    prefix="/get_events"
)

@router.get('')
async def route():
    return await EventService().get_all_events()