# Backend of Food Recommender
***
## Introduction
This is backend part of Indian food recommender web app. It is implemented in python using Django Framework.
Gunicorn server is used as a gateway to forward Nginx's `/api` requests to Django server.
***
## Implementation
This Django project contains a django app `api` which handles all the REST api request and returns results.

The api endpoint `/api/recommender` receives image and location data. 

The image is sent to `food_image_recognition` module and it predicts the dish using pre trained model.

The predictions received from `food_image_recognition` module and location data is passed into `recommeder` module which finds the restaurants and return a list of Restaurants. 

This data is then sent to the client.
***
## How deep learning model was trained ?
The code for model training is in  `food_image_recognition` folder, with two jupyter notebooks.

1. `prepare.ipynb` file contains the code for preprocessing the image data.
2. `model_creation.ipynb` file contains the code for deep learning model creation and training.

Note: Model creation and training was done on https://colab.research.google.com
