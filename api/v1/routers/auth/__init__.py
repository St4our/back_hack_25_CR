from fastapi import APIRouter

from .login import router as router_login
from .register import router as router_register
from .verify_code import router as router_verify_code
from .auth_from_rsaag import router as router_auth_rsaag

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

routers = [router_login, router_register, router_verify_code, router_auth_rsaag]
[router.include_router(_router) for _router in routers]
