from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, BackgroundTasks

from api.services.base import BaseService
from db.models import User
from passlib.hash import pbkdf2_sha512

class UserService(BaseService):
    """
    CRUD для управления пользователями
    """
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, name: str, email: str, password: str, is_admin: bool = False, bg_tasks: BackgroundTasks = None):
        """
        Создание нового пользователя
        """
        existing_user = await self.get(self.db, User, email=email)
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        password_hash = pbkdf2_sha512.hash(password)
        user = await self.create_model(self.db, User, name=name, email=email, password_hash=password_hash, is_admin=is_admin)
        return user

    async def get(self, user_id: int = None, email: str = None):
        """
        Получение пользователя по ID или email
        """
        filters = {}
        if user_id:
            filters["id"] = user_id
        if email:
            filters["email"] = email

        user = await self.get(self.db, User, **filters)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def get_all(self):
        """
        Получение списка всех пользователей
        """
        users = await self.get_all(self.db, User)
        return users

    async def delete(self, user_id: int):
        """
        Удаление пользователя
        """
        await self.delete_model(self.db, User, id=user_id)
        return {"status": "ok", "message": "User deleted"}
