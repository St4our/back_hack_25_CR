from fastapi import APIRouter

from .awards import router as router_awards
from .events import router as router_events
from .fighter import router as router_fighters
from .municipality import router as router_municipalities
from .userlogs import router as router_userlogs
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger


app = FastAPI(
    title='Admin panel',
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(
    prefix="/admin_panel",
    tags=["Admin_panel"]
)

routers = [router_awards, router_events, router_fighters, router_municipalities, router_userlogs]
[router.include_router(_router) for _router in routers]

app.include_router(router)

def create_app():
    logger.debug('Starting API ...')
    return app



