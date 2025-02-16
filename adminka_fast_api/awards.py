from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from adminka_fast_api.services.award import AwardService
from db.models.awards import Award

router = APIRouter(
    prefix="/awards",
    tags=["awards"]
)

# Pydantic модели для запросов и ответов
class AwardCreateSchema(BaseModel):
    name: str
    photo_path: Optional[str] = None
    description: Optional[str] = None

class AwardUpdateSchema(BaseModel):
    name: Optional[str] = None
    photo_path: Optional[str] = None
    description: Optional[str] = None

class AwardResponseSchema(BaseModel):
    id: int
    name: str
    photo_path: Optional[str] = None
    description: Optional[str] = None

# Инициализация сервиса
award_service = AwardService()

# Роут для получения награды по ID
@router.get("/{award_id}", response_model=AwardResponseSchema)
async def get_award(award_id: int):
    """
    Получить награду по ID
    """
    result = await award_service.get_award(award_id)
    return result['award']

# Роут для получения всех наград
@router.get("/", response_model=List[AwardResponseSchema])
async def get_all_awards():
    """
    Получить все награды
    """
    result = await award_service.get_all_awards()
    return result['awards']

# Роут для поиска наград по названию
@router.get("/search/", response_model=dict)
async def search_awards(
    query: str = Query(..., description="Поисковый запрос"),
    limit: int = Query(10, description="Лимит результатов"),
    page: int = Query(1, description="Номер страницы")
):
    """
    Поиск наград по названию
    """
    result = await award_service.search_awards(query, limit, page)
    return result

# Роут для создания новой награды
@router.post("/", response_model=dict)
async def create_award(award_data: AwardCreateSchema):
    """
    Создать новую награду
    """
    result = await award_service.create(
        name=award_data.name,
        photo_path=award_data.photo_path,
        description=award_data.description
    )
    return result

# Роут для обновления награды
@router.put("/{award_id}", response_model=dict)
async def update_award(award_id: int, award_data: AwardUpdateSchema):
    """
    Обновить информацию о награде
    """
    result = await award_service.update(
        id=award_id,
        name=award_data.name,
        photo_path=award_data.photo_path,
        description=award_data.description
    )
    return result

# Роут для удаления награды
@router.delete("/{award_id}", response_model=dict)
async def delete_award(award_id: int):
    """
    Удалить награду
    """
    result = await award_service.delete(award_id)
    return result