from flask import request, jsonify
from flask_restful import Resource
from admin.models.user import User
from models.base import db
from pydantic import BaseModel, ValidationError

class UserSchema(BaseModel):
    name: str
    email: str
    password_hash: str
    is_admin: bool
    last_code: str = None

class UserResource(Resource):
    def get(self, user_id):
        """Получить пользователя по ID"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return {"id": user.id, "name": user.name, "email": user.email, "is_admin": user.is_admin}, 200

    def delete(self, user_id):
        """Удалить пользователя"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200

class UserListResource(Resource):
    def get(self):
        """Получить всех пользователей"""
        users = User.query.all()
        return [{"id": u.id, "name": u.name, "email": u.email, "is_admin": u.is_admin} for u in users], 200

    def post(self):
        """Создать нового пользователя"""
        try:
            data = UserSchema(**request.json)
        except ValidationError as e:
            return {"error": e.errors()}, 400

        user = User(name=data.name, email=data.email, password_hash=data.password_hash, is_admin=data.is_admin, last_code=data.last_code)
        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "message": "User created"}, 201
