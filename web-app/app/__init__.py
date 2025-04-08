"""
Initializes flask and mongodb app
"""

import os

from dotenv import load_dotenv
from flask import Flask
from .extensions import mongo, db, bcrypt, login_manager


def create_app():
    """
    initizes everything that will be used
    """
    load_dotenv()
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.secret_key = os.getenv("SECRET_KEY")
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from .auth import auth  # pylint: disable=import-outside-toplevel
    from .routes import main  # pylint: disable=import-outside-toplevel

    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
