import cv2
import numpy as np
from tensorflow.keras.models import load_model
import base64
from flask import current_app

MODEL = load_model("model/asl_cnn.h5")

def preprocess_image_from_frame(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    processed = np.expand_dims(resized.astype("float32"), axis=-1)
    processed = np.expand_dims(processed, axis=0)
    return processed

def predict_asl_letter(frame_data):
    # Remove potential header if not already stripped
    if "," in frame_data:
        frame_data = frame_data.split(",")[1]
    img_bytes = base64.b64decode(frame_data)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Save debug image (optional)
    # cv2.imwrite("debug_input.jpg", img)

    processed = preprocess_image_from_frame(img)
    
    # Save a visualization of the processed image for debugging (scaled for display)
    # cv2.imwrite("debug_processed.jpg", processed[0][:, :, 0] * 255)
    
    preds = MODEL.predict(processed)
    current_app.logger.info("Raw predictions: %s", preds)
    predicted_class = np.argmax(preds, axis=1)[0]
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prediction = letters[predicted_class] if predicted_class < len(letters) else "Unknown"
    current_app.logger.info("Predicted class index: %s, letter: %s", predicted_class, prediction)
    return prediction
