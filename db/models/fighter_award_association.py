from sqlalchemy import Column, Integer, ForeignKey, Table
from ..base_model import Model

fighter_award_association = Table(
    'fighter_award', Model.metadata,
    Column('fighter_id', Integer, ForeignKey('fighters.id', ondelete='CASCADE'), primary_key=True),
    Column('award_id', Integer, ForeignKey('awards.id', ondelete='CASCADE'), primary_key=True)
)