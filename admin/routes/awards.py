from flask import request, jsonify
from flask_restful import Resource
from models.award import Award
from models.base import db
from pydantic import ValidationError
from pydantic import BaseModel
from typing import Optional

class AwardSchema(BaseModel):
    name: str
    photo_path: Optional[str] = None
    description: Optional[str] = None

class AwardResource(Resource):
    def get(self, award_id):
        """Получить награду по ID"""
        award = Award.query.get(award_id)
        if not award:
            return {"message": "Award not found"}, 404
        return {"id": award.id, "name": award.name, "photo_path": award.photo_path, "description": award.description}, 200

    def delete(self, award_id):
        """Удалить награду"""
        award = Award.query.get(award_id)
        if not award:
            return {"message": "Award not found"}, 404
        db.session.delete(award)
        db.session.commit()
        return {"message": "Award deleted"}, 200

class AwardListResource(Resource):
    def get(self):
        """Получить все награды"""
        awards = Award.query.all()
        return [{"id": a.id, "name": a.name, "photo_path": a.photo_path, "description": a.description} for a in awards], 200

    def post(self):
        """Создать новую награду"""
        try:
            data = AwardSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        award = Award(name=data.name, photo_path=data.photo_path, description=data.description)
        db.session.add(award)
        db.session.commit()
        return {"id": award.id, "message": "Award created"}, 201

class AwardUpdateResource(Resource):
    def put(self, award_id):
        """Обновить награду"""
        award = Award.query.get(award_id)
        if not award:
            return {"message": "Award not found"}, 404

        try:
            data = AwardSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        award.name = data.name
        award.photo_path = data.photo_path
        award.description = data.description

        db.session.commit()
        return {"message": "Award updated", "id": award.id}, 200
