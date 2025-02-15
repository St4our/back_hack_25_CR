from flask import Flask
from flask_restful import Api
from models.base import db
from routes.main_routes import register_api
from config_db import Config_db

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config_db)  # Загружаем конфигурацию с путём к БД

db.init_app(app)


register_api(api)

if __name__ == "__main__":
    app.run(debug=True)
