"""
Provides routes for main flask app
"""

from flask import Blueprint, render_template, request, jsonify, current_app
from flask_login import login_required, current_user
from datetime import datetime
from flask import Blueprint, request, jsonify
from .predictor import predict_asl_letter
from .extensions import db
import traceback

main = Blueprint("main", __name__)
bp = Blueprint("predict", __name__)


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
def upload_frame():
    data = request.get_json(force=True)
    if "frame_data" not in data:
        return jsonify({"error": "No frame data provided."}), 400
    if "user_id" not in data:
        return jsonify({"error": "No user id provided."}), 400

    frame_data = data["frame_data"]

    # Clean the frame data by removing the data URL prefix, if it exists.
    try:
        if frame_data.startswith("data:image/jpeg;base64,"):
            frame_data = frame_data.split("data:image/jpeg;base64,")[1]
    except Exception as e:
        current_app.logger.error("Frame data processing failed: %s", traceback.format_exc())
        return jsonify({"error": f"Frame data processing failed: {str(e)}"}), 500

    try:
        predicted_letter = predict_asl_letter(frame_data)
    except Exception as e:
        current_app.logger.error("Prediction failed: %s", traceback.format_exc())
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

    new_entry = {
        "user_id": data["user_id"],
        "predicted_letter": predicted_letter,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    result = db.predicted_letters.insert_one(new_entry)
    print("Inserted document ID:", result.inserted_id)
    return jsonify({
        "success": True,
        "predicted_letter": predicted_letter,
        "entry_id": str(result.inserted_id)
    }), 200