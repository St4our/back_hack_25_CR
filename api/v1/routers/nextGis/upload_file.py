from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
import os

from api.services.nextGis import  upload_file

router = APIRouter(
    prefix="/upload_file"
)

@router.post("")
async def upload_file_route(file: UploadFile = File(...)):
    file_path = os.path.join('uploads', file.filename)
    try:
        with open(file_path, 'wb') as f:
            content = await file.read()
            f.write(content)
        
        uploaded_file = await upload_file(file_path, file.filename)
        return JSONResponse(content=uploaded_file, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))