from .models.base import db
from sqlalchemy.orm import relationship
from .models.fighter_award_association import fighter_award_association

class Award(db.Model):
    """
    Модель награды
    """
    __tablename__ = "awards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    photo_path = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)

    fighters = relationship("Fighter", secondary=fighter_award_association, back_populates="awards")
