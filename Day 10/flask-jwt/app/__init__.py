from flask import Flask
from .db import db
from .routes import auth_bp
from flask_jwt_extended import JWTManager
from config import Config
# from cors import CORS 



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/user')

    return app
