from fastapi import APIRouter

from .edit_text import router as router_edit_text
from .enhance_image import router as router_enchance_image

router = APIRouter(
    prefix="/fiches",
    tags=["Fiches"]
)

routers = [router_edit_text, router_enchance_image]
[router.include_router(_router) for _router in routers]
