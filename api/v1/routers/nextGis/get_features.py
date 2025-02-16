from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from api.services.nextGis import get_features, utm_to_coord

router = APIRouter(
    prefix="/get_features"
)


@router.get("/get_features")
async def get_features_route(layer_id: int):
    """Получение всех фичей с автоматической конвертацией координат"""
    try:
        features = await get_features(layer_id)
        
        for feature in features:
            geom = feature.get("geom")
            if geom and "POINT" in geom:
                utm_x, utm_y = map(float, geom.replace("POINT(", "").replace(")", "").split())
                lon, lat = utm_to_coord(utm_x, utm_y)
                feature["geom"] = f"POINT ({lon} {lat})"

        return JSONResponse(content=features, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))