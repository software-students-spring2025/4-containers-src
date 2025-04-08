"""
dependencies that prevent circular import
"""

# app/extensions.py
import os
import pymongo
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Load environment variables early
load_dotenv()

# Initialize shared extensions
mongo = pymongo.MongoClient(os.getenv("MONGO_URI"), ssl=True)
db = mongo[os.getenv("MONGO_DBNAME")]
bcrypt = Bcrypt()
login_manager = LoginManager()
