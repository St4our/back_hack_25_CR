from fastapi import APIRouter

from .remove import router as router_remove
from .change_password import router as router_change_password
from .create import router as router_create_log
from .get_all_logs import router as router_get_all_logs
from .get_log import router as router_get_log

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

routers = [router_remove, router_change_password, router_create_log, router_get_log, router_get_all_logs]
[router.include_router(_router) for _router in routers]
