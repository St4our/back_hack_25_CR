from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from api.services.nextGis import get_features

router = APIRouter(
    prefix="/get_features"
)


@router.get("")
async def get_features_route(layer_id: int):
    try:
        features = await get_features(layer_id)
        return JSONResponse(content=features, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))