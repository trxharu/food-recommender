import json
import os
import overpass

class RestaurantNotFountException(Exception):
    pass

def getRecommendation(location, food_prediction):
    api = overpass.API("https://z.overpass-api.de/api/interpreter", timeout=1000)

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

    cuisine = data[food_prediction.strip()]
    # getting a list of restaurants near given location in 5km radius
    overpass_query = f'node["amenity"="restaurant"]["cuisine"={cuisine}](around:3000.0, {locatn["lat"]}, {locatn["lng"]});'
    
    try:
        response = api.get(overpass_query)
        if len(response.features) == 0:
            raise RestaurantNotFountException("Couldn't get any restaurants near you.")
        return response.features
    except RestaurantNotFountException as err:
        raise Exception(err)
    except Exception as err:
        raise Exception(err)


