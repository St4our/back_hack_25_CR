from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from api.services.events import EventService
from db.models.events import Event

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
    result = await event_service.get_event(event_id)
    return result['event']

@router.get("/", response_model=List[EventResponseSchema])
async def get_all_events():
    """
    Получить все события
    """
    result = await event_service.get_all_events()
    return result['events']

@router.post("/", response_model=dict)
async def create_event(event_data: EventCreateSchema):
    """
    Создать новое событие
    """
    result = await event_service.create(
        title=event_data.title,
        info=event_data.info
    )
    return result

@router.put("/{event_id}", response_model=dict)
async def update_event(event_id: int, event_data: EventUpdateSchema):
    """
    Обновить информацию о событии
    """
    result = await event_service.update(
        id=event_id,
        title=event_data.title,
        info=event_data.info
    )
    return result

@router.delete("/{event_id}", response_model=dict)
async def delete_event(event_id: int):
    """
    Удалить событие
    """
    result = await event_service.delete(event_id)
    return result