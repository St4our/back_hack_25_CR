from fastapi import APIRouter

from .get_events import router as router_events

router = APIRouter(
    prefix="/event",
    tags=["Event"]
)

routers = [router_events]
[router.include_router(_router) for _router in routers]
