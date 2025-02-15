from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Dict

from api.services.nextGis import  attach_file

router = APIRouter(
    prefix="/attach_file"
)

@router.post("")
async def attach_file_route(data: Dict):
    layer_id = data['layer_id']
    feature_id = data['feature_id']
    file_data = data['file_data']
    try:
        attached_file = await attach_file(layer_id, feature_id, file_data)
        return JSONResponse(content=attached_file, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))