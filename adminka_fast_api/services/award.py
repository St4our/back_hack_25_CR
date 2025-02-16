from fastapi import HTTPException
from api.services.base import BaseService
from db.models.awards import Award

class AwardService:
    """
    Сервис для работы с наградами
    """
    def __init__(self):
        self.model = Award

    @staticmethod
    async def generate_award_dict(award: Award) -> dict:
        """
        Генерация информации о награде в виде словаря
        """
        if not award:
            return {}
        return {
            'id': award.id,
            'name': award.name,
            'photo_path': award.photo_path,
            'description': award.description
        }
    
    async def get_award(self, id: int) -> dict:
        """
        Получение награды по id
        """
        award = await BaseService().get(self.model, id=id)
        if not award:
            raise HTTPException(status_code=404, detail="Award not found")
        return {'status': 'ok', 'award': await self.generate_award_dict(award)}
    
    async def get_all_awards(self) -> dict:
        """
        Получение всех наград
        """
        awards = await BaseService().get_all(self.model)
        return {'status': 'ok', 'awards': [await self.generate_award_dict(award) for award in awards]}
    
    async def search_awards(self, query: str, limit: int = 0, page: int = 1) -> dict:
        """
        Поиск наград по названию
        """
        custom_where = self.model.name.ilike(f"%{query}%")
        awards, count = await BaseService().search(self.model, custom_where=custom_where, limit=limit, page=page)
        return {'status': 'ok', 'count': count, 'awards': [await self.generate_award_dict(award) for award in awards]}

    async def create(self, name: str, photo_path: str, description: str) -> dict:
        """
        Создание новой награды
        """
        award = await BaseService().create(self.model, name=name, photo_path=photo_path, description=description)
        return {'status': 'ok', 'award_id': award.id}
    
    async def delete(self, id: int) -> dict:
        """
        Удаление награды
        """
        await BaseService().delete(self.model, id=id)
        return {'status': 'ok'}
    
    async def update(self, id: int, name: str, photo_path: str, description: str) -> dict:
        """
        Обновление информации о награде
        """
        award = await BaseService().get(self.model, id=id)
        if not award:
            raise HTTPException(status_code=404, detail="Award not found")
        
        award.name = name
        award.photo_path = photo_path
        award.description = description
        
        updated_award = await BaseService().update(award)
        return {'status': 'ok', 'award': await self.generate_award_dict(updated_award)}