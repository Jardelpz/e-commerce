FROM python:3.8-slim-buster

MAINTAINER Jardel Pereira Zermiani

ADD . /app

WORKDIR /app

RUN apt-get update && apt-get install


RUN pip install --no-cache -U && pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "src.app:app"]