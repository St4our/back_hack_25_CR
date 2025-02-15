from fastapi import HTTPException
from api.services.base import BaseService
from db.models.user_logs import UserLog


class UserLogService:
    """
    Сервис для работы с логами пользователей
    """
    def __init__(self):
        self.model = UserLog

    @staticmethod
    async def generate_user_log_dict(user_log: UserLog) -> dict:
        """
        Генерация информации о логе пользователя в виде словаря
        """
        if not user_log:
            return {}
        return {
            "id": user_log.id,
            "user_id": user_log.user_id,
            "fighter_id": user_log.fighter_id,
        }

    async def get_log(self, id: int) -> dict:
        """
        Получение лога по id
        """
        log = await BaseService().get(self.model, id=id)
        if not log:
            raise HTTPException(status_code=404, detail="Log not found")
        return {"status": "ok", "log": await self.generate_user_log_dict(log)}

    async def get_all_logs(self) -> dict:
        """
        Получение всех логов
        """
        logs = await BaseService().get_all(self.model)
        return {
            "status": "ok",
            "logs": [await self.generate_user_log_dict(log) for log in logs],
        }

    async def search_logs(self, user_id: int = None, fighter_id: int = None, limit: int = 0, page: int = 1) -> dict:
        """
        Поиск логов по user_id и fighter_id
        """
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if fighter_id:
            filters["fighter_id"] = fighter_id

        logs, count = await BaseService().search(self.model, limit=limit, page=page, **filters)
        return {
            "status": "ok",
            "count": count,
            "logs": [await self.generate_user_log_dict(log) for log in logs],
        }

    async def create(self, user_id: int, fighter_id: int) -> dict:
        """
        Создание нового лога пользователя
        """
        log = await BaseService().create(self.model, user_id=user_id, fighter_id=fighter_id)
        return {"status": "ok", "log_id": log.id}

    async def delete(self, id: int) -> dict:
        """
        Удаление лога
        """
        await BaseService().delete(self.model, id=id)
        return {"status": "ok"}
