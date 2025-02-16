from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from api.services.municipality import MunicipalityService
from db.models.municipalities import Municipality

router = APIRouter(
    prefix="/municipalities",
    tags=["municipalities"]
)

# Pydantic модели для запросов и ответов
class MunicipalityCreateSchema(BaseModel):
    title: str

class MunicipalityUpdateSchema(BaseModel):
    title: Optional[str] = None

class MunicipalityResponseSchema(BaseModel):
    id: int
    title: str

municipality_service = MunicipalityService()

@router.get("/{municipality_id}", response_model=MunicipalityResponseSchema)
async def get_municipality(municipality_id: int):
    """
    Получить муниципалитет по ID
    """
    result = await municipality_service.get_municipality(municipality_id)
    return result['municipality']

@router.get("/", response_model=List[MunicipalityResponseSchema])
async def get_all_municipalities():
    """
    Получить все муниципалитеты
    """
    result = await municipality_service.get_all_municipalities()
    return result['municipalities']

@router.post("/", response_model=dict)
async def create_municipality(municipality_data: MunicipalityCreateSchema):
    """
    Создать новый муниципалитет
    """
    result = await municipality_service.create(
        title=municipality_data.title
    )
    return result

@router.put("/{municipality_id}", response_model=dict)
async def update_municipality(municipality_id: int, municipality_data: MunicipalityUpdateSchema):
    """
    Обновить информацию о муниципалитете
    """
    result = await municipality_service.update(
        id=municipality_id,
        title=municipality_data.title
    )
    return result

@router.delete("/{municipality_id}", response_model=dict)
async def delete_municipality(municipality_id: int):
    """
    Удалить муниципалитет
    """
    result = await municipality_service.delete(municipality_id)
    return result