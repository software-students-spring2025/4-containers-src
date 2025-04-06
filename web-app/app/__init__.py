"""
Initializes flask and mongodb app
"""
import os

import pymongo
from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

load_dotenv()

mongo = pymongo.MongoClient(os.getenv("MONGO_URI"), ssl = True)
db = mongo[os.getenv("MONGO_DBNAME")]
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    """
    initizes everything that will be used
    """
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.secret_key = os.getenv("SECRET_KEY")
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from .auth import auth # pylint: disable=import-outside-toplevel
    from .routes import main # pylint: disable=import-outside-toplevel
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
