import json
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
    res = {"msg": "i got your image"}
    imageFile = request.FILES['image']

    imageFile = imageFile.read()

    predictions = predict(imageFile)
    print(predictions)

    return HttpResponse(json.dumps(res), content_type='application/json')
