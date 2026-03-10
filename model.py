import tensorflow as tf
import numpy as np
from PIL import Image

<<<<<<< HEAD
# โหลดโมเดล
model = tf.keras.applications.MobileNetV2(weights="imagenet")

def predict(image: Image):

    image = image.resize((224, 224))
=======
model = tf.keras.applications.MobileNetV2(weights="imagenet")

def predict(image):
    
    image = image.resize((224,224))
>>>>>>> 9cf9d7371dad60d05a0fa3a907a1a775304724e8
    image = np.array(image)

    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)

    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)

    return decoded[0][0][1]