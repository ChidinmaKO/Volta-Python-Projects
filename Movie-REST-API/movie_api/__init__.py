from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from movie_api.config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from movie_api.routes import main

    app.register_blueprint(main)

    return app