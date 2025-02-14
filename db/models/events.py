from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.models.fighter_event_association import fighter_event_association

from db.base_model import Model

class Event(Model):
    """
    Модель события
    """
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    info = Column(String, nullable=True)

    fighters = relationship('Fighter', secondary=fighter_event_association, back_populates='events')
