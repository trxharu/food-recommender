from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

a_file = open("classes.txt", "r")
class_names = a_file.readlines()
a_file.close()


def predict(image_data):
    model = load_model('keras_model.h5')

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_data)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array
    # run the inference
    prediction = model.predict(data)[0]

    preds = np.array(prediction)
    top_five = preds.argsort()[::-1][:5]
    top_five_preds = []

    for i in top_five:
        top_five_preds.append({"dish": class_names[i], "confidence": preds[i] * 100})

    return top_five_preds
