from fastapi import APIRouter, HTTPException, File, UploadFile
import os

from api.services.nextGis import  upload_file

router = APIRouter(
    prefix="/upload_file"
)

@router.post("")
async def upload_file_route(file: UploadFile = File(...)):
    """ Загрузка файла на сервер """
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())

        uploaded_file = await upload_file(file_path, file.filename)
        return {"status": "success", "uploaded_file": uploaded_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
