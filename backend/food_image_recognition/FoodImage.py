import io
import os
from keras.models import load_model
from PIL import ImageOps, Image
import numpy as np


def predict(image_data):
    workdir = os.path.dirname(__file__)

    classes_path = os.path.join(workdir, "classes.txt")
    model_path = os.path.join(workdir, "keras_model.h5")

    # Loading Classes data
    file = open(classes_path, "r")
    class_names = file.readlines()
    file.close()

    # Loading Model data
    model = load_model(model_path)

    # Preprocessing image
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(io.BytesIO(image_data))

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    # Predicting image class using pretrained model
    prediction = model.predict(data)[0]

    preds = np.array(prediction)
    top_five = preds.argsort()[::-1][:5]
    top_five_preds = []

    for i in top_five:
        top_five_preds.append(
            {"dish": class_names[i], "accuracy": preds[i] * 100})

    return top_five_preds
