from flask import request, jsonify
from flask_restful import Resource
from admin.models.event import Event
from admin.models.base import db
from pydantic import ValidationError
from pydantic import BaseModel
from typing import Optional

class EventSchema(BaseModel):
    title: str
    info: Optional[str] = None

class EventResource(Resource):
    def get(self, event_id):
        """Получить событие по ID"""
        event = Event.query.get(event_id)
        if not event:
            return {"message": "Event not found"}, 404
        return {"id": event.id, "title": event.title, "info": event.info}, 200

    def delete(self, event_id):
        """Удалить событие"""
        event = Event.query.get(event_id)
        if not event:
            return {"message": "Event not found"}, 404
        db.session.delete(event)
        db.session.commit()
        return {"message": "Event deleted"}, 200

class EventListResource(Resource):
    def get(self):
        """Получить все события"""
        events = Event.query.all()
        return [{"id": e.id, "title": e.title, "info": e.info} for e in events], 200

    def post(self):
        """Создать новое событие"""
        try:
            data = EventSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        event = Event(title=data.title, info=data.info)
        db.session.add(event)
        db.session.commit()
        return {"id": event.id, "message": "Event created"}, 201

class EventUpdateResource(Resource):
    def put(self, event_id):
        """Обновить событие"""
        event = Event.query.get(event_id)
        if not event:
            return {"message": "Event not found"}, 404

        try:
            data = EventSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        event.title = data.title
        event.info = data.info

        db.session.commit()
        return {"message": "Event updated", "id": event.id}, 200
