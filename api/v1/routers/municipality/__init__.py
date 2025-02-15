from fastapi import APIRouter

from .get_municipalities import router as router_municipalities
from .get_municipality import router as router_municipalities

router = APIRouter(
    prefix="/municipality",
    tags=["Municipality"]
)

routers = [router_municipalities]
[router.include_router(_router) for _router in routers]
