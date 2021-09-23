FROM python
WORKDIR /backend
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install django tensorflow opencv-python overpass gunicorn numpy
COPY . .