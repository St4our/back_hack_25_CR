from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base import db

class Municipality(db.Model):
    """
    Модель муниципалитета
    """
    __tablename__ = "municipalities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)

    fighters = relationship('Fighter', back_populates='municipality')
