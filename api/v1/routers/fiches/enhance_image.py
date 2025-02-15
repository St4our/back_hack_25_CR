from fastapi import APIRouter
from fastapi import UploadFile, File
from api.services.fiches import enhance_image

router = APIRouter(
    prefix="/enhance_image"
)


@router.post("")
async def enhance_uploaded_image(file: UploadFile = File(...)):
    image_data = await file.read()
    enhanced_image = enhance_image(image_data)
    return {"filename": file.filename, "enhanced_image": enhanced_image}