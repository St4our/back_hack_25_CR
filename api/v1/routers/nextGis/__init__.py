from fastapi import APIRouter

from .add_feature import router as router_add_feature
from .attach_file import router as router_attach_file
from .get_features import router as router_get_features
from .upload_file import router as router_upload_file

router = APIRouter(
    prefix="/nextGis",
    tags=["NextGis"]
)

routers = [router_add_feature, router_attach_file, router_get_features, router_upload_file]
[router.include_router(_router) for _router in routers]
