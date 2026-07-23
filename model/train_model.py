import tensorflow as tf
import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# ============================================
# Configuration
# ============================================

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 15

TRAIN_DIR = "dataset/train"
VAL_DIR = "dataset/val"

# ============================================
# Data Generators
# ============================================

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(
    rescale=1.0 / 255
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

validation_generator = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# ============================================
# Save Class Names
# ============================================

class_names = list(train_generator.class_indices.keys())

with open("model/class_names.json", "w") as f:
    json.dump(class_names, f, indent=4)

print("✅ Class names saved.")

# ============================================
# Load MobileNetV2
# ============================================

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

base_model.trainable = False

# ============================================
# Build Model
# ============================================

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)

output = Dense(
    train_generator.num_classes,
    activation="softmax"
)(x)

model = Model(
    inputs=base_model.input,
    outputs=output
)

# ============================================
# Compile
# ============================================

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# ============================================
# Callbacks
# ============================================

callbacks = [

    EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    ),

    ModelCheckpoint(
        filepath="model/plant_model.keras",
        monitor="val_accuracy",
        save_best_only=True
    )

]

# ============================================
# Train
# ============================================

print("\n🚀 Training Started...\n")

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    callbacks=callbacks
)

print("\n✅ Training Completed!")

# ============================================
# Save Final Model
# ============================================

model.save("model/plant_model.keras")

print("✅ Model saved successfully!")