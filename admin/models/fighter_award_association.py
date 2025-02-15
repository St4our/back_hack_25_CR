from .models.base import db

fighter_award_association = db.Table(
    'fighter_award',
    db.Column('fighter_id', db.Integer, db.ForeignKey('fighters.id', ondelete='CASCADE'), primary_key=True),
    db.Column('award_id', db.Integer, db.ForeignKey('awards.id', ondelete='CASCADE'), primary_key=True)
)
