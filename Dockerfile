FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8000

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV CUDA_VISIBLE_DEVICES=-1

CMD python3 app.py
