from fastapi import APIRouter, Depends

from api.services.fighter import FighterService
from db.models import User
from api.utils import get_current_user

router = APIRouter(
    prefix="/create"
)

@router.post('')
async def route(user: User = Depends(get_current_user)):
    return await FighterService().create(user_id=user.id)
