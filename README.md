# Indian Food Recommender (based on location)
***
## Introduction
This is a Image Recognition project for recognizing indian foods from 80 different classes and also show available restaurants around you using your location. (based on image dataset provided by kaggle, link is in references section of this readme)

***
## Implementation
The backend part of the web app is created using Django Framework, to know more about backend implementation read `backend`'s README.

The frontend part is build using React Js with Typescript and then build, static files from build are served on Nginx Web server. To know more about frontend implementation read `frontend`'s README.
***
## Architecture
![image](https://gitlab.com/trxharudev/food-recommender/-/raw/master/images/architecture.drawio.png)

***
## Requirements
Before getting started, make sure you meet following requirements.

1. Docker or (Docker for Windows)
2. Git
3. docker-compose (if you are not using windows)
4. Internet Connection to build images

## Getting Started

1. Clone this repo using `git clone https://gitlab.com/trxharudev/food-recommender.git`.
2. Goto the cloned directory using `cd food-recommender`.
3. Run `docker-compose up` to start the frontend and backend server.
4. To close the server run `docker-compose down` in another terminal.

## Run some examples

`examples` folder contains few images that can be used for testing. Open README for examples to know how to use.
***
## References 
1. Image Dataset provided by Kaggle - https://www.kaggle.com/iamsouravbanerjee/indian-food-images-dataset
2. Location Search is provided by OpenStreetMap's Overpass API - https://wiki.openstreetmap.org/wiki/Overpass_API
