"""
Provides routes for main flask app
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import datetime

from .extensions import db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """
    home page, regardless whether user is logged in or not
    """
    return render_template("home.html")


@main.route("/camera")
def camera():
    """
    camera to record hand movements
    """
    return render_template("camera.html")

@main.route("/upload_frame", methods=["POST"])
@login_required
def upload_frame():
    data = request.get_json()
    if not data or "frame_data" not in data:
        return jsonify({"error": "No frame data provided"}), 400

    frame_data = data["frame_data"]
    user_id = current_user.id

    frame_record = {
        "user_id": user_id,
        "frame_data": frame_data,
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    }
    
    result = db.frames.insert_one(frame_record)
    
    return jsonify({"success": True, "frame_id": str(result.inserted_id)})