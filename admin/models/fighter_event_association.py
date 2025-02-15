from .models.base import db

fighter_event_association = db.Table(
    'fighter_event',
    db.Column('fighter_id', db.Integer, db.ForeignKey('fighters.id', ondelete='CASCADE'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'), primary_key=True)
)
