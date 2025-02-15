from fastapi import APIRouter
from fastapi import HTTPException
from typing import Dict, Any
from pydantic import BaseModel

from api.services.nextGis import add_feature

router = APIRouter(
    prefix="/add_feature"
)

class FeatureCreateSchema(BaseModel):
    layer_id: int
    feature_data: Dict[str, Any]


@router.post("", response_model=Dict)
async def add_feature_route(data: FeatureCreateSchema):
    """ Добавление новой записи (фичи) в слой """
    try:
        added_feature = await add_feature(data.layer_id, data.feature_data)
        return {"status": "success", "feature": added_feature}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
