from fastapi import APIRouter

from .get_awards import router as router_awards

router = APIRouter(
    prefix="/award",
    tags=["Award"]
)

routers = [router_awards]
[router.include_router(_router) for _router in routers]
