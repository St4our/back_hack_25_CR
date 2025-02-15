from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from admin.models.base import db

class User(db.Model):
    """
    Модель пользователя
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    last_code = Column(String, nullable=True)

    logs = relationship("UserLog", back_populates="user", cascade="all, delete-orphan")
