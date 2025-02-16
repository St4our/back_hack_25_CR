from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.email_service import send_mes


router = APIRouter(
    prefix="/ask_on_email"
)

class Message(BaseModel):
    text: str

@router.post("")
async def send_email(message: Message):
    try:
        send_mes(message.text)
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
