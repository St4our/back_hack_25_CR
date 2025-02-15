from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base_model import Model

class UserLog(Model):
    """
    Модель логов для пользователей
    """
    __tablename__ = "users_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    fighter_id = Column(Integer, ForeignKey("fighters.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User", back_populates="logs")
    fighter = relationship("Fighter", back_populates="logs")
