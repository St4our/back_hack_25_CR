from fastapi import APIRouter

from .get_municipalities import router as router_municipalities

router = APIRouter(
    prefix="/municipality",
    tags=["Event"]
)

routers = [router_municipalities]
[router.include_router(_router) for _router in routers]
