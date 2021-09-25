import json
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from food_image_recognition.FoodImage import predict
from recommender.FoodRecommender import getRecommendation


def welcome(request):
    data = {"msg": "This is a Food recommendation API."}
    return HttpResponse(json.dumps(data),
                        content_type='application/json')


@csrf_exempt
def getRecommendations(request):
    res = {"status": ""}

    imageFile = request.FILES['image']
    imageFile = imageFile.read()
    prediction, acc = predict(imageFile)
    recomms = getRecommendation(request.POST["location"], prediction)

    if (len(recomms) != 0):
        res["status"] = "OK"
        res["predictions"] = { "dish": prediction, "accuracy": ceil(acc) }
        res["data"] = recomms
    else:
        res["status"] = "FAIL"
        res["predictions"] = { "dish": prediction, "accuracy": ceil(acc) }
        res["msg"] = "Couldn't get restaurants near you that serve this food."

    return HttpResponse(json.dumps(res), content_type='application/json')
