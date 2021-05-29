FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

RUN pip install -U pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app