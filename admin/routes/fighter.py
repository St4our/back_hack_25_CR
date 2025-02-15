from flask import request, jsonify
from flask_restful import Resource
from models.fighter import Fighter
from models.base import db
from pydantic import ValidationError
from pydantic import BaseModel
from typing import Optional, List

class EventSchema(BaseModel):
    id: int
    title: str
    info: Optional[str] = None

class AwardSchema(BaseModel):
    id: int
    name: str
    photo_path: Optional[str] = None
    description: Optional[str] = None

class FighterSchema(BaseModel):
    name: str
    birth_death_years: str
    municipality_id: Optional[int] = None
    short_info: Optional[str] = None
    is_accept: Optional[bool] = False
    photo_path: Optional[str] = None
    awards: Optional[List[AwardSchema]] = []
    events: Optional[List[EventSchema]] = []

class FighterResource(Resource):
    def get(self, fighter_id):
        """Получить бойца по ID с наградами и событиями"""
        fighter = Fighter.query.get(fighter_id)
        if not fighter:
            return {"message": "Fighter not found"}, 404
        
        return {
            "id": fighter.id, 
            "name": fighter.name, 
            "birth_death_years": fighter.birth_death_years,
            "municipality_id": fighter.municipality_id,
            "short_info": fighter.short_info,
            "is_accept": fighter.is_accept,
            "photo_path": fighter.photo_path,
            "awards": [{"id": a.id, "name": a.name, "photo_path": a.photo_path, "description": a.description} for a in fighter.awards],
            "events": [{"id": e.id, "title": e.title, "info": e.info} for e in fighter.events]
        }, 200

    def delete(self, fighter_id):
        """Удалить бойца"""
        fighter = Fighter.query.get(fighter_id)
        if not fighter:
            return {"message": "Fighter not found"}, 404
        db.session.delete(fighter)
        db.session.commit()
        return {"message": "Fighter deleted"}, 200

class FighterListResource(Resource):
    def get(self):
        """Получить всех бойцов с наградами и событиями"""
        fighters = Fighter.query.all()
        return [
            {
                "id": f.id, 
                "name": f.name, 
                "birth_death_years": f.birth_death_years,
                "municipality_id": f.municipality_id,
                "short_info": f.short_info,
                "is_accept": f.is_accept,
                "photo_path": f.photo_path,
                "awards": [{"id": a.id, "name": a.name, "photo_path": a.photo_path, "description": a.description} for a in f.awards],
                "events": [{"id": e.id, "title": e.title, "info": e.info} for e in f.events]
            } 
            for f in fighters
        ], 200

    def post(self):
        """Создать нового бойца"""
        try:
            data = FighterSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        fighter = Fighter(
            name=data.name, 
            birth_death_years=data.birth_death_years,
            municipality_id=data.municipality_id,
            short_info=data.short_info,
            is_accept=data.is_accept,
            photo_path=data.photo_path
        )

        # Добавляем награды
        if data.awards:
            from models.award import Award
            for award_data in data.awards:
                award = Award.query.get(award_data.id)
                if award:
                    fighter.awards.append(award)

        # Добавляем события
        if data.events:
            from models.event import Event
            for event_data in data.events:
                event = Event.query.get(event_data.id)
                if event:
                    fighter.events.append(event)

        db.session.add(fighter)
        db.session.commit()
        return {"id": fighter.id, "message": "Fighter created"}, 201

class FighterUpdateResource(Resource):
    def put(self, fighter_id):
        """Обновить бойца и его связи"""
        fighter = Fighter.query.get(fighter_id)
        if not fighter:
            return {"message": "Fighter not found"}, 404

        try:
            data = FighterSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        fighter.name = data.name
        fighter.birth_death_years = data.birth_death_years
        fighter.municipality_id = data.municipality_id
        fighter.short_info = data.short_info
        fighter.is_accept = data.is_accept
        fighter.photo_path = data.photo_path

        from models.award import Award
        fighter.awards.clear()
        if data.awards:
            for award_data in data.awards:
                award = Award.query.get(award_data.id)
                if award:
                    fighter.awards.append(award)

        from models.event import Event
        fighter.events.clear()
        if data.events:
            for event_data in data.events:
                event = Event.query.get(event_data.id)
                if event:
                    fighter.events.append(event)

        db.session.commit()
        return {"message": "Fighter updated", "id": fighter.id}, 200
