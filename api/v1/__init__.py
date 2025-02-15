from fastapi import APIRouter

from .routers.health import router as router_health
from .routers.auth import router as router_auth
from .routers.users import router as router_users
from .routers.award import router as router_awards
from .routers.event import router as router_events
from .routers.fighter import router as router_fighter
from .routers.municipality import router as router_municipality


router = APIRouter(
    prefix="/v1",
    tags=["V1"]
)

routers = [router_health, router_auth, router_users, router_awards, router_events, router_fighter, router_municipality]
[router.include_router(_router) for _router in routers]
