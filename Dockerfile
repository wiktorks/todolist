FROM python:3.10.4

RUN mkdir /app
COPY ./requirements.txt /app


RUN pip install -r /app/requirements.txt

WORKDIR /app