from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.services.nextGis import get_features, utm_to_coord

router = APIRouter(prefix="/get_features")

@router.get("/")
async def get_features_route(layer_id: int):
    """Получение всех фичей с автоматической конвертацией координат"""
    try:
        features = await get_features(layer_id)

        if not isinstance(features, list):  # Проверяем, что API вернул список
            raise HTTPException(status_code=500, detail="Invalid API response format")

        for feature in features:
            geom = feature.get("geom")
            if geom and geom.startswith("POINT"):
                try:
                    coords = geom.replace("POINT(", "").replace(")", "").strip().split()
                    utm_x, utm_y = map(float, coords)
                    lon, lat = utm_to_coord(utm_x, utm_y)
                    feature["geom"] = f"POINT ({lon} {lat})"
                except ValueError:
                    feature["geom"] = "Invalid geometry"

        return JSONResponse(content={"status": "ok", "features": features}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
