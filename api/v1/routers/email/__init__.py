from fastapi import APIRouter

from .ask_on_email import router as router_ask_on_email

router = APIRouter(
    prefix="/email",
    tags=["Email"]
)

routers = [router_ask_on_email]
[router.include_router(_router) for _router in routers]
