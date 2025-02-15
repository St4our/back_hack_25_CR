from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .models.base import db
from .models.fighter_event_association import fighter_event_association
from .models.fighter_award_association import fighter_award_association

class Fighter(db.Model):
    """
    Модель бойца
    """
    __tablename__ = "fighters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birth_death_years = Column(String, nullable=False)
    municipality_id = Column(Integer, ForeignKey("municipalities.id", ondelete="SET NULL"))
    short_info = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)

    municipality = relationship("Municipality", back_populates="fighters")
    awards = relationship("Award", secondary=fighter_award_association, back_populates="fighters")
    events = relationship("Event", secondary=fighter_event_association, back_populates="fighters")
    logs = relationship("UserLog", back_populates="fighter")

