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
mongo = pymongo.MongoClient(os.getenv("MONGO_URI", "mongodb://admin:secretpassword@localhost:27017/gesture_auth?authSource=admin"), ssl=True)
db = mongo[os.getenv("MONGO_DBNAME", "test_db")]
bcrypt = Bcrypt()
login_manager = LoginManager()
