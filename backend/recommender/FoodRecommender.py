import json
import os
import overpass


def getRecommendation(location, food_predictions):
    api = overpass.API(
        "https://lz4.overpass-api.de/api/interpreter", timeout=300)

    workdir = os.path.dirname(__file__)
    cuisine_data = os.path.join(workdir, "cuisine_data.txt")

    locatn = json.loads(location)

    # Loading data for cuisine in food classes
    files = open(cuisine_data, "r")
    classes = files.readlines()
    files.close()

    data = {}

    for cl in classes:
        temp = cl.split(",")
        data[temp[0]] = temp[1].strip()

    cuisine = data[food_predictions[0]["dish"].strip()]
    # getting a list of restaurants near given location in 5km radius
    overpass_query = f'node["amenity"="restaurant"]["cuisine"={cuisine}](around:3000.0, {locatn["lat"]}, {locatn["lng"]});'
    response = api.get(overpass_query)

    return response.features
