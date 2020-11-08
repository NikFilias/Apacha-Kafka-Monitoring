FROM python:3.7-alpine

WORKDIR /usr/src/app

RUN pip install kafka-python

COPY . .

CMD ["python3","./kafka-producer.py"]