import json
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from food_image_recognition.FoodImage import predict
from recommender.FoodRecommender import getRecommendation


@csrf_exempt
def getRecommendations(request):
    # Response object
    res = {"status": ""}

    # Extracting image file from HTTP request
    imageFile = request.FILES['image']
    imageFile = imageFile.read()

    # Predicting image using image recognition module
    prediction, acc = predict(imageFile)

    try:
        recomms = getRecommendation(request.POST["location"], prediction)
        res["status"] = "OK"
        res["predictions"] = { "dish": prediction, "accuracy": ceil(acc) }
        res["data"] = recomms
    except Exception as err:
        res["status"] = "FAIL"
        res["predictions"] = { "dish": prediction, "accuracy": ceil(acc) }
        res["msg"] = str(err)
            
    return HttpResponse(json.dumps(res), content_type='application/json')
