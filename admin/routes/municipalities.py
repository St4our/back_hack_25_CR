from flask import request, jsonify
from flask_restful import Resource
from models.municipality import Municipality
from models.base import db
from pydantic import ValidationError
from pydantic import BaseModel
from typing import Optional

class MunicipalitySchema(BaseModel):
    title: str 

class MunicipalityService:
    """
    Сервис для работы с муниципалитетами
    """
    @staticmethod
    def generate_municipality_dict(municipality: Municipality) -> dict:
        """
        Генерация информации о муниципалитете в виде словаря
        """
        if not municipality:
            return {}
        return {
            'id': municipality.id,
            'title': municipality.title
        }

class MunicipalityResource(Resource):
    def get(self, municipality_id):
        """Получить муниципалитет по ID"""
        municipality = Municipality.query.get(municipality_id)
        if not municipality:
            return {"message": "Municipality not found"}, 404
        return {"id": municipality.id, "title": municipality.title}, 200

    def delete(self, municipality_id):
        """Удалить муниципалитет"""
        municipality = Municipality.query.get(municipality_id)
        if not municipality:
            return {"message": "Municipality not found"}, 404
        db.session.delete(municipality)
        db.session.commit()
        return {"message": "Municipality deleted"}, 200

class MunicipalityListResource(Resource):
    def get(self):
        """Получить все муниципалитеты"""
        municipalities = Municipality.query.all()
        return [{"id": m.id, "title": m.title} for m in municipalities], 200

    def post(self):
        """Создать новый муниципалитет"""
        try:
            data = MunicipalitySchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        municipality = Municipality(title=data.title)
        db.session.add(municipality)
        db.session.commit()
        return {"id": municipality.id, "message": "Municipality created"}, 201

class MunicipalityUpdateResource(Resource):
    def put(self, municipality_id):
        """Обновить информацию о муниципалитете"""
        municipality = Municipality.query.get(municipality_id)
        if not municipality:
            return {"message": "Municipality not found"}, 404

        try:
            data = MunicipalitySchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        municipality.title = data.title
        db.session.commit()
        return {"message": "Municipality updated", "id": municipality.id}, 200