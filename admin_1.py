"""from flask import Flask
from flask_restful import Api
from admin.models.base import db
from admin.config import Config
from api import register_api

admin = Flask(__name__)
admin.config.from_object(Config)

db.init_app(admin)
api = Api(admin)

# Регистрируем API
register_api(api)

# Создаем таблицы
with admin.app_context():
    db.create_all()

if __name__ == "__main__":
    admin.run(debug=True)"""
