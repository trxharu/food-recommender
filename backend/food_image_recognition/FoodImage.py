import io
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input


def predict(image_file):
    workdir = os.path.dirname(__file__)

    classes_path = os.path.join(workdir, "classes.txt")
    model_path = os.path.join(workdir, "63_food_recom.h5")
    
    img_data = io.BytesIO(image_file).getvalue()
    img = np.fromstring(img_data, dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (224, 224))

    img_ex = np.expand_dims(img, axis=0)
    input_img = preprocess_input(img_ex)

    model = load_model(model_path)
    predictions = model.predict(input_img)

    top_index = np.argmax(predictions)

    with open(classes_path, "r") as f:
        class_names = f.readlines()
        f.close()

    return class_names[top_index], (predictions[0][top_index] * 100)
