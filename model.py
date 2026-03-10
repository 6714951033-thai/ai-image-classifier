import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.applications.MobileNetV2(weights="imagenet")

def predict(image):
    
    image = image.resize((224,224))
    image = np.array(image)

    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)

    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)

    return decoded[0][0][1]