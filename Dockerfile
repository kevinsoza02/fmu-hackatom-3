FROM python:3.12-slim as build

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir poetry
RUN poetry install

FROM python:3.12-slim as production

