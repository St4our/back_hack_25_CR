from fastapi import APIRouter

from .upload_file import router as router_upload_file
from .get_file import router as router_get_file

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

routers = [router_upload_file, router_get_file]
[router.include_router(_router) for _router in routers]
