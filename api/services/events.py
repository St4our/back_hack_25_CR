from fastapi import HTTPException
from api.services.base import BaseService
from db.models.events import Event

class EventService:
    """
    Сервис для работы с событиями
    """
    def __init__(self):
        self.model = Event

    @staticmethod
    async def generate_event_dict(event: Event) -> dict:
        """
        Генерация информации о событии в виде словаря
        """
        if not event:
            return {}
        return {
            'id': event.id,
            'title': event.title,
            'info': event.info
        }
    
    async def get_event(self, id: int) -> dict:
        """
        Получение события по id
        """
        event = await BaseService().get(self.model, id=id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return {'status': 'ok', 'event': await self.generate_event_dict(event)}
    
    async def get_all_events(self) -> dict:
        """
        Получение всех событий
        """
        events = await BaseService().get_all(self.model)
        return {'status': 'ok', 'events': [await self.generate_event_dict(event) for event in events]}
    
    async def create(self, title: str, info: str) -> dict:
        """
        Создание нового события
        """
        event = await BaseService().create(self.model, title=title, info=info)
        return {'status': 'ok', 'event_id': event.id}
    
    async def delete(self, id: int) -> dict:
        """
        Удаление события
        """
        await BaseService().delete(self.model, id=id)
        return {'status': 'ok'}
    
    async def update(self, id: int, title: str, info: str) -> dict:
        """
        Обновление информации о событии
        """
        event = await BaseService().get(self.model, id=id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        
        event.title = title
        event.info = info
        
        updated_event = await BaseService().update(event)
        return {'status': 'ok', 'event': await self.generate_event_dict(updated_event)}