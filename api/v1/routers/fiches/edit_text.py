from fastapi import APIRouter
from pydantic import BaseModel
from services.fiches import edit_text_gpt


router = APIRouter(
    prefix="/edit_text"
)

class EditTextRequest(BaseModel):
    text: str

class EditTextResponse(BaseModel):
    original_text: str
    edited_text: str

@router.post("", response_model=EditTextResponse)
async def edit_text(request: EditTextRequest):
    edited_text = edit_text_gpt(request.text)
    return EditTextResponse(original_text=request.text, edited_text=edited_text)