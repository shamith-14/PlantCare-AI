import numpy as np
from tensorflow.keras.preprocessing import image


IMG_SIZE = (224, 224)


def preprocess_image(image_path):
    """
    Load and preprocess an image for prediction.
    """

    img = image.load_img(image_path, target_size=IMG_SIZE)

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array