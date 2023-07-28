#!/bin/bash

FROM python:3.11

WORKDIR /tiktak

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "--app=src/flaskr", "run", "--host=0.0.0.0", "--port=1234"]
