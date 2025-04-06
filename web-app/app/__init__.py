from flask import Flask
#get rid of one or the other
from flask_pymongo import PyMongo
import pymongo
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

load_dotenv()

#mongo = PyMongo()
mongo = pymongo.MongoClient(os.getenv("MONGO_URI"), ssl = True)
db = mongo[os.getenv("MONGO_DBNAME")]
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    

    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    #testing
    print("MONGO_URI:", app.config["MONGO_URI"])
    app.secret_key = os.getenv("SECRET_KEY")

    #mongo.init_app(app)

    #test
    print(type(db))

    bcrypt.init_app(app)
    login_manager.init_app(app)

    #login_manager.login_view = "auth.login"

    from .auth import auth
    from .routes import main
        
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app