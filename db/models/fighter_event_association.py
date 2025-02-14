from sqlalchemy import Column, Integer, ForeignKey, Table
from ..base_model import Model

fighter_event_association = Table(
    'fighter_event', Model.metadata,
    Column('fighter_id', Integer, ForeignKey('fighters.id', ondelete='CASCADE'), primary_key=True),
    Column('event_id', Integer, ForeignKey('events.id', ondelete='CASCADE'), primary_key=True)
)