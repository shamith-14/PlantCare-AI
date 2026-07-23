import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report

# Load the trained model
model = load_model("model/plant_model.keras")

# Validation dataset path
VAL_DIR = "dataset/val"

# Image settings (must match training)
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Load validation images
val_datagen = ImageDataGenerator(rescale=1./255)

val_generator = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# Predict classes
predictions = model.predict(val_generator)

predicted_classes = np.argmax(predictions, axis=1)

true_classes = val_generator.classes

class_labels = list(val_generator.class_indices.keys())

# Print Classification Report
print("\nClassification Report:\n")
print(classification_report(
    true_classes,
    predicted_classes,
    target_names=class_labels
))
