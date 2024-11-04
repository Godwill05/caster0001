# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from .models.user import User  # Gardez l'importation du modèle User ici

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Charge l'utilisateur par son ID

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.config.from_object(Config)

    db.init_app(app)  # Initialise db ici
    login_manager.init_app(app)

    with app.app_context():
        # Crée les tables dans la base de données
        db.create_all()

        from .controllers import post_bp
        from .controllers.main import main

        app.register_blueprint(main)
        app.register_blueprint(post_bp)

    return app
