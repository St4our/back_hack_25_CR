from fastapi import APIRouter

from .get_fighters import router as router_fighters
from .get_fighter import router as router_fighter
from .create import router as router_create_fighter

router = APIRouter(
    prefix="/fighter",
    tags=["Fighter"]
)

routers = [router_fighter, router_fighters, router_create_fighter]
[router.include_router(_router) for _router in routers]
