from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Dict

from api.services.nextGis import add_feature

router = APIRouter(
    prefix="/add_feature"
)

@router.post("")
async def add_feature_route(data: Dict):
    layer_id = data['layer_id']
    feature_data = data['feature_data']
    try:
        added_feature = await add_feature(layer_id, feature_data)
        return JSONResponse(content=added_feature, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))