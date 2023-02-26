# Some Examples on How to use this Web App

This folder contains few random dish images from google images.

***
## 1. aloo_gobi
Click on the button `Select an Image File` and provide location access.

![image](https://github.com/cyr1Lprog/food-recommender/blob/main/images/1.png)

**Note:** If you can't see any map, then it is likely that Overpass API has no data on your location. Try to fake location for some popular place like New Delhi ( latitude: 28.6079, longitude: 77.2063 ) in developer console in browser.
***
## 2. jalebi
After faking location and clicking on button `Select an Image File`, you will get results in a map. Where **Blue** marker is your current location and **Green** markers are locations of restaurants.

![image](https://github.com/cyr1Lprog/food-recommender/blob/main/images/2.png)

**Note:** Refresh the page to use another example.
***
## 3. lassi
As the deep learning model is trained on 80 classes of foods, some foods can be recognized with 100% accuracy despite having 63% model accuracy.

![image](https://github.com/cyr1Lprog/food-recommender/blob/main/images/3.png)
***
## 4. matar_paneer
And some indian foods looks similar to other foods, and can be wrongly recognized.

![image](https://github.com/cyr1Lprog/food-recommender/blob/main/images/4.png)
***

## 5. steak
What happens when a food which the model has not trained on ? It will still work but cannot predict correctly.

![image](https://github.com/cyr1Lprog/food-recommender/blob/main/images/5.png)