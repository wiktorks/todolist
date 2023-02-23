FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir -p /app/temp

COPY ./django/ /app

RUN pip install -r requirements.txt
