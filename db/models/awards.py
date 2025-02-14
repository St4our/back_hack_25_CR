from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.base_model import Model
from db.models.fighter_award_association import fighter_award_association


class Award(Model):
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    photo_path = Column(String)
    description = Column(String)

    # 👇 Вот эта связь должна быть
    fighters = relationship("Fighter", secondary=fighter_award_association, back_populates="awards")
