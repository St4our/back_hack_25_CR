from fastapi import HTTPException
from api.services.base import BaseService
from db.models.municipalities import Municipality

class MunicipalityService:
    """
    Сервис для работы с муниципалитетами
    """
    def __init__(self):
        self.model = Municipality

    @staticmethod
    async def generate_municipality_dict(municipality: Municipality) -> dict:
        """
        Генерация информации о муниципалитете в виде словаря
        """
        if not municipality:
            return {}
        return {
            'id': municipality.id,
            'title': municipality.title
        }
    
    async def get_municipality(self, id: int) -> dict:
        """
        Получение муниципалитета по id
        """
        municipality = await BaseService().get(self.model, id=id)
        if not municipality:
            raise HTTPException(status_code=404, detail="Municipality not found")
        return {'status': 'ok', 'municipality': await self.generate_municipality_dict(municipality)}
    
    async def get_all_municipalities(self) -> dict:
        """
        Получение всех муниципалитетов
        """
        municipalities = await BaseService().get_all(self.model)
        return {
            'status': 'ok',
            'municipalities': [await self.generate_municipality_dict(municipality) for municipality in municipalities]
        }
    
    async def create(self, title: str) -> dict:
        """
        Создание нового муниципалитета
        """
        municipality = await BaseService().create(self.model, title=title)
        return {'status': 'ok', 'municipality_id': municipality.id}
    
    async def delete(self, id: int) -> dict:
        """
        Удаление муниципалитета
        """
        await BaseService().delete(self.model, id=id)
        return {'status': 'ok'}
    
    async def update(self, id: int, title: str) -> dict:
        """
        Обновление информации о муниципалитете
        """
        municipality = await BaseService().get(self.model, id=id)
        if not municipality:
            raise HTTPException(status_code=404, detail="Municipality not found")
        
        municipality.title = title
        
        updated_municipality = await BaseService().update(municipality)
        return {'status': 'ok', 'municipality': await self.generate_municipality_dict(updated_municipality)}
