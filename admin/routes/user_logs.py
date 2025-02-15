from flask import request, jsonify
from flask_restful import Resource
from admin.models.user_log import UserLog
from admin.models.base import db
from pydantic import BaseModel, ValidationError

class UserLogSchema(BaseModel):
    user_id: int
    fighter_id: int

class UserLogResource(Resource):
    def get(self, log_id):
        """Получить лог пользователя по ID"""
        log = UserLog.query.get(log_id)
        if not log:
            return {"message": "UserLog not found"}, 404
        return {"id": log.id, "user_id": log.user_id, "fighter_id": log.fighter_id}, 200

    def delete(self, log_id):
        """Удалить лог пользователя"""
        log = UserLog.query.get(log_id)
        if not log:
            return {"message": "UserLog not found"}, 404
        db.session.delete(log)
        db.session.commit()
        return {"message": "UserLog deleted"}, 200

class UserLogListResource(Resource):
    def get(self):
        """Получить все логи пользователей"""
        logs = UserLog.query.all()
        return [{"id": log.id, "user_id": log.user_id, "fighter_id": log.fighter_id} for log in logs], 200

    def post(self):
        """Создать новый лог для пользователя"""
        try:
            data = UserLogSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        log = UserLog(user_id=data.user_id, fighter_id=data.fighter_id)
        db.session.add(log)
        db.session.commit()
        return {"id": log.id, "message": "UserLog created"}, 201
