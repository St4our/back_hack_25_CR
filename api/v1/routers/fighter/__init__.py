from fastapi import APIRouter

from .get_fighters import router as router_fighters
from .get_fighter import router as router_fighter
from .verify_code import router as router_verify_code

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

routers = [router_fighter, router_fighters, router_verify_code]
[router.include_router(_router) for _router in routers]
