FROM python:slim
ENV TF_CPP_MIN_LOG_LEVEL=2
WORKDIR /backend
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . .
RUN pip --no-cache-dir install -r req.txt