from fastapi import APIRouter

from .routers.health import router as router_health
from .routers.auth import router as router_auth
from .routers.users import router as router_users
from .routers.award import router as router_awards
from .routers.event import router as router_events
from .routers.fighter import router as router_fighter
from .routers.municipality import router as router_municipality
from .routers.nextGis import router as router_nextGis
from .routers.fiches import router as router_fiches
from .routers.email import router as router_email
from .routers.files import router as router_files
from .routers.userLogs import router as router_userLogs


router = APIRouter(
    prefix="/v1",
    tags=["V1"]
)

routers = [router_health, router_auth, router_users, router_awards, router_events, router_fighter, router_municipality, router_nextGis, router_fiches, router_email, router_files, router_userLogs]
[router.include_router(_router) for _router in routers]
