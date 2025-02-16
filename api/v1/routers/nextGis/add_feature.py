from fastapi import APIRouter
from fastapi import HTTPException
from typing import Dict, Any
from pydantic import BaseModel

from api.services.nextGis import add_feature, coord_to_utm

router = APIRouter(
    prefix="/add_feature"
)

class FeatureCreateSchema(BaseModel):
    layer_id: int
    feature_data: Dict[str, Any]

@router.post("", response_model=Dict)
async def add_feature_route(data: FeatureCreateSchema):
    """Добавление новой записи (фичи) в слой с автоматической конвертацией координат"""
    try:
        geom = data.feature_data.get("geom")
        if geom and "POINT" in geom:
            lon, lat = map(float, geom.replace("POINT(", "").replace(")", "").split())
            utm_x, utm_y = coord_to_utm(lon, lat)
            data.feature_data["geom"] = f"POINT ({utm_x} {utm_y})"

        added_feature = await add_feature(data.layer_id, data.feature_data)
        return {"status": "success", "feature": added_feature}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))