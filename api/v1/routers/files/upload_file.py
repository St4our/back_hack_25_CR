from fastapi import APIRouter, UploadFile, File
import shutil
import os
from config import upload_dir


router = APIRouter(
    prefix="/upload_file"
)

@router.post("")
async def upload_file(file: UploadFile = File(...)):
    """
    Загружает файл и сохраняет его в папке `static/`
    """
    file_path = os.path.join(upload_dir, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "url": f"/files/{file.filename}"}