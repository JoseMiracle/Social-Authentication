FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
