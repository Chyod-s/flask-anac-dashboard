FROM python:3-alpine3.20

WORKDIR /api-flask

# copiar arquivos nescessarios
COPY . /api-flask

RUN pip3 install - upgrade pip && pip install --no-cache-dir - r requirements.txt
