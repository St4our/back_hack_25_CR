from sqlalchemy import Column, Integer, String, ForeignKey
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
    name = Column(String, nullable=False)
    birth_death_years = Column(String, nullable=False)
    municipality_id = Column(Integer, ForeignKey("municipalities.id", ondelete="SET NULL"), nullable=True)
    short_info = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)

    user = relationship("User", back_populates="logs")
    fighter = relationship("Fighter", back_populates="logs")
