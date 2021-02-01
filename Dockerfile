FROM python:3.8-slim-buster

WORKDIR /srv

RUN apt-get update && apt-get install


ADD requirements.txt /srv/

ADD . /srv


RUN pip install --no-cache -U && pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "src.app:app"]