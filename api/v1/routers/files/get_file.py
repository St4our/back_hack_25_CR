from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from config import settings
import os

upload_dir = settings.upload_dir


router = APIRouter(
    prefix="/get_file"
)

@router.get("/{filename}")
async def get_file(filename: str):
    """
    Возвращает файл по имени
    """
    file_path = os.path.join(upload_dir, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)