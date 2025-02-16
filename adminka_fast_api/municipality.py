from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from adminka_fast_api.services.municipality import MunicipalityService
from db.models.municipalities import Municipality
from adminka_fast_api import logger  # Импорт логгера

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
    logger.info(f"Запрос: Получение муниципалитета ID {municipality_id}")
    result = await municipality_service.get_municipality(municipality_id)
    logger.info(f"Ответ: {result}")
    return result['municipality']

@router.get("/", response_model=List[MunicipalityResponseSchema])
async def get_all_municipalities():
    """
    Получить все муниципалитеты
    """
    logger.info("Запрос: Получение всех муниципалитетов")
    result = await municipality_service.get_all_municipalities()
    logger.info(f"Найдено муниципалитетов: {len(result['municipalities'])}")
    return result['municipalities']

@router.post("/", response_model=dict)
async def create_municipality(municipality_data: MunicipalityCreateSchema):
    """
    Создать новый муниципалитет
    """
    logger.info(f"Запрос: Создание муниципалитета - {municipality_data.title}")
    result = await municipality_service.create(
        title=municipality_data.title
    )
    logger.info(f"Муниципалитет создан: {result}")
    return result

@router.put("/{municipality_id}", response_model=dict)
async def update_municipality(municipality_id: int, municipality_data: MunicipalityUpdateSchema):
    """
    Обновить информацию о муниципалитете
    """
    logger.info(f"Запрос: Обновление муниципалитета ID {municipality_id} - данные: {municipality_data}")
    result = await municipality_service.update(
        id=municipality_id,
        title=municipality_data.title
    )
    logger.info(f"Муниципалитет обновлен: {result}")
    return result

@router.delete("/{municipality_id}", response_model=dict)
async def delete_municipality(municipality_id: int):
    """
    Удалить муниципалитет
    """
    logger.info(f"Запрос: Удаление муниципалитета ID {municipality_id}")
    result = await municipality_service.delete(municipality_id)
    logger.info(f"Муниципалитет удален: {result}")
    return result
