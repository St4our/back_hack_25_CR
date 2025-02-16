from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from adminka_fast_api.services.events import EventService
from db.models.events import Event
from adminka_fast_api import logger  # Импорт логгера

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

# Pydantic модели для запросов и ответов
class EventCreateSchema(BaseModel):
    title: str
    info: Optional[str] = None

class EventUpdateSchema(BaseModel):
    title: Optional[str] = None
    info: Optional[str] = None

class EventResponseSchema(BaseModel):
    id: int
    title: str
    info: Optional[str] = None

event_service = EventService()

@router.get("/{event_id}", response_model=EventResponseSchema)
async def get_event(event_id: int):
    """
    Получить событие по ID
    """
    logger.info(f"Запрос: Получение события ID {event_id}")
    result = await event_service.get_event(event_id)
    logger.info(f"Ответ: {result}")
    return result['event']

@router.get("/", response_model=List[EventResponseSchema])
async def get_all_events():
    """
    Получить все события
    """
    logger.info("Запрос: Получение всех событий")
    result = await event_service.get_all_events()
    logger.info(f"Найдено событий: {len(result['events'])}")
    return result['events']

@router.post("/", response_model=dict)
async def create_event(event_data: EventCreateSchema):
    """
    Создать новое событие
    """
    logger.info(f"Запрос: Создание события - {event_data.title}")
    result = await event_service.create(
        title=event_data.title,
        info=event_data.info
    )
    logger.info(f"Событие создано: {result}")
    return result

@router.put("/{event_id}", response_model=dict)
async def update_event(event_id: int, event_data: EventUpdateSchema):
    """
    Обновить информацию о событии
    """
    logger.info(f"Запрос: Обновление события ID {event_id} - данные: {event_data}")
    result = await event_service.update(
        id=event_id,
        title=event_data.title,
        info=event_data.info
    )
    logger.info(f"Событие обновлено: {result}")
    return result

@router.delete("/{event_id}", response_model=dict)
async def delete_event(event_id: int):
    """
    Удалить событие
    """
    logger.info(f"Запрос: Удаление события ID {event_id}")
    result = await event_service.delete(event_id)
    logger.info(f"Событие удалено: {result}")
    return result
