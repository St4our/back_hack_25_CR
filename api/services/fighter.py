from fastapi import HTTPException
from api.services.base import BaseService
from db.models.fighters import Fighter
from db.models.user_logs import UserLog



class FighterService:
    """
    Сервис для работы с бойцами
    """
    def __init__(self):
        self.model = Fighter

    @staticmethod
    async def generate_fighter_dict(fighter: Fighter) -> dict:
        """
        Генерация информации о бойце в виде словаря
        """
        if not fighter:
            return {}
        return {
            'id': fighter.id,
            'name': fighter.name,
            'birth_death_years': fighter.birth_death_years,
            'municipality_id': fighter.municipality_id,
            'short_info': fighter.short_info,
            'photo_path': fighter.photo_path,
            'awards': [{'id': award.id, 'name': award.name} for award in fighter.awards],
            'events': [{'id': event.id, 'title': event.title} for event in fighter.events]
        }
    
    async def get_fighter(self, id: int) -> dict:
        """
        Получение бойца по id
        """
        fighter = await BaseService().get(self.model, id=id)
        if not fighter:
            raise HTTPException(status_code=404, detail="Fighter not found")
        return {'status': 'ok', 'fighter': await self.generate_fighter_dict(fighter)}
    
    async def get_all_fighters(self) -> dict:
        """
        Получение всех бойцов
        """
        fighters = await BaseService().get_all(self.model)
        return {'status': 'ok', 'fighters': [await self.generate_fighter_dict(fighter) for fighter in fighters]}
    
    async def search_fighters(self, query: str, limit: int = 0, page: int = 1) -> dict:
        """
        Поиск бойцов по названию
        """
        custom_where = self.model.name.ilike(f"%{query}%")
        awards, count = await BaseService().search(self.model, custom_where=custom_where, limit=limit, page=page)
        return {'status': 'ok', 'count': count, 'awards': [await self.generate_award_dict(award) for award in awards]}


    async def create(self, user_id: int, name: str, birth_death_years: str, municipality_id: int, short_info: str, photo_path: str) -> dict:
        """
        Создание нового бойца и запись в user_logs
        """
        fighter = await BaseService().create(
            self.model,
            name=name,
            birth_death_years=birth_death_years,
            municipality_id=municipality_id,
            short_info=short_info,
            photo_path=photo_path
        )


        await BaseService().create(
            UserLog,
            user_id=user_id,
            fighter_id=fighter.id
        )

        return {'status': 'ok', 'fighter_id': fighter.id}
    
    async def delete(self, id: int) -> dict:
        """
        Удаление бойца
        """
        await BaseService().delete(self.model, id=id)
        return {'status': 'ok'}
    
    async def update(self, id: int, name: str, birth_death_years: str, short_info: str, photo_path: str) -> dict:
        """
        Обновление информации о бойце
        """
        fighter = await BaseService().get(self.model, id=id)
        if not fighter:
            raise HTTPException(status_code=404, detail="Fighter not found")
        
        fighter.name = name
        fighter.birth_death_years = birth_death_years
        fighter.short_info = short_info
        fighter.photo_path = photo_path
        
        updated_fighter = await BaseService().update(fighter)
        return {'status': 'ok', 'fighter': await self.generate_fighter_dict(updated_fighter)}