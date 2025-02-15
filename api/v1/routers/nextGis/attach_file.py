from fastapi import APIRouter
from fastapi import HTTPException
from typing import Dict
from pydantic import BaseModel

from api.services.nextGis import  attach_file

router = APIRouter(
    prefix="/attach_file"
)

from pydantic import BaseModel
from typing import Dict


class FileUploadSchema(BaseModel):
    id: str
    size: int


class FileDataSchema(BaseModel):
    size: int
    name: str
    mime_type: str
    file_upload: FileUploadSchema


class AttachFileSchema(BaseModel):
    layer_id: int
    feature_id: int
    file_data: FileDataSchema


@router.post("")
async def attach_file_route(data: AttachFileSchema):
    """ Прикрепление загруженного файла к записи (фиче) """
    try:
        attached_file = await attach_file(data.layer_id, data.feature_id, data.file_data)
        return {"status": "success", "attached_file": attached_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))