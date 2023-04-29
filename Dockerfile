FROM python:3.10-slim-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

COPY app ./app

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
