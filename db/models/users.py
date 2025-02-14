from sqlalchemy import Column, String, Integer, Boolean

from db.base_model import Model

class User(Model):
    """
    Модель пользователя
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)
    last_code = Column(String, nullable=True)