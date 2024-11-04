# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_cle_secrete'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'    # ceci permet de creer la base de donne local dans un dossier instannce et qui est securisé
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"  # Chemin de la base de données
    SQLALCHEMY_TRACK_MODIFICATIONS = False
