from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from fastapi import BackgroundTasks

from api.services.user import UserService

router = APIRouter(
    prefix="/register"
)

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

@router.post('')
async def route(schema: RegisterSchema, bg_tasks: BackgroundTasks):
    return await UserService().create(name=schema.name, email=schema.email, password=schema.password, bg_tasks=bg_tasks)
