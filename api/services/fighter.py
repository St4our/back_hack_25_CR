from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from db.models.fighters import Fighter
from db.models.user_logs import UserLog
from api.services.base import BaseService
from db.database import get_db
from fastapi import Query

class FighterService:
    """
    Сервис для работы с бойцами
    """

    def __init__(self, db: AsyncSession):
        self.db = db
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
            'municipality_id': fighter.municipality.title,
            'short_info': fighter.short_info,
            'photo_path': fighter.photo_path,
            'awards': [{'id': award.id, 'name': award.name} for award in (fighter.awards or [])],
            'events': [{'id': event.id, 'title': event.title} for event in (fighter.events or [])]
        }

    async def get_fighter(self, id: int):
        """ Получение одного бойца по ID с названием района """
        result = await self.db.execute(
            select(Fighter)
            .options(
                joinedload(Fighter.awards),
                joinedload(Fighter.events),
                joinedload(Fighter.municipality)  # Загружаем объект района
            )
            .filter(Fighter.id == id)
        )
        fighter = result.scalars().first()

        if not fighter:
            raise HTTPException(status_code=404, detail="Fighter not found")

        return {
            'status': 'ok',
            'fighter': await self.generate_fighter_dict(fighter)
        }

    async def get_all_fighters(self, name: str = None, municipality_id: int = None):
        """ Получение всех бойцов с возможностью фильтрации и названием района """
        query = select(Fighter).options(
            joinedload(Fighter.awards),
            joinedload(Fighter.events),
            joinedload(Fighter.municipality)  # Загружаем объект района
        ).order_by(Fighter.id.desc())

        if name and name.strip():
            query = query.filter(Fighter.name.ilike(f"%{name}%"))

        if municipality_id is not None:
            query = query.filter(Fighter.municipality_id == municipality_id)

        result = await self.db.execute(query)
        fighters = result.unique().scalars().all()

        return {
            'status': 'ok',
            'fighters': [await self.generate_fighter_dict(fighter) for fighter in fighters]
        }

    async def create(self, user_id: int, name: str, birth_death_years: str, municipality_id: int, short_info: str, photo_path: str) -> dict:
        """ Создание нового бойца и запись в user_logs """
        fighter = await BaseService(self.db).create(
            self.model,
            name=name,
            birth_death_years=birth_death_years,
            municipality_id=municipality_id,
            short_info=short_info,
            photo_path=photo_path
        )

        await BaseService(self.db).create(
            UserLog,
            user_id=user_id,
            fighter_id=fighter.id
        )

        return {'status': 'ok', 'fighter_id': fighter.id}

    async def delete(self, id: int) -> dict:
        """ Удаление бойца """
        await BaseService(self.db).delete(self.model, id=id)
        return {'status': 'ok'}

    async def update(self, id: int, name: str, birth_death_years: str, short_info: str, photo_path: str) -> dict:
        """ Обновление информации о бойце """
        fighter = await BaseService(self.db).get(self.model, id=id)
        if not fighter:
            raise HTTPException(status_code=404, detail="Fighter not found")

        fighter.name = name
        fighter.birth_death_years = birth_death_years
        fighter.short_info = short_info
        fighter.photo_path = photo_path

        updated_fighter = await BaseService(self.db).update(fighter)
        return {'status': 'ok', 'fighter': await self.generate_fighter_dict(updated_fighter)}
