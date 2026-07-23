import json
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from model.utils import preprocess_image

# Load trained model
model = load_model("model/plant_model.keras")

# Load class names
with open("model/class_names.json", "r") as f:
    class_names = json.load(f)


def predict_disease(image_path):
    """
    Predict plant disease from an uploaded image.

    Args:
        image_path (str): Path to uploaded image

    Returns:
        tuple:
            disease_name (str)
            confidence (float)
    """

    # Preprocess image
    img = preprocess_image(image_path)

    # Predict
    prediction = model.predict(img, verbose=0)

    # Highest probability class
    predicted_index = np.argmax(prediction)

    # Confidence score
    confidence = float(np.max(prediction) * 100)

    # Disease name
    disease = class_names[predicted_index]

    # Format for display
    disease = disease.replace("___", " - ")
    disease = disease.replace("_", " ")


    return disease, confidence