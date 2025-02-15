from .models.base import db
from sqlalchemy.orm import relationship
from .models.fighter_event_association import fighter_event_association

class Event(db.Model):
    """
    Модель события
    """
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    info = db.Column(db.String, nullable=True)

    fighters = relationship("Fighter", secondary=fighter_event_association, back_populates="events")
