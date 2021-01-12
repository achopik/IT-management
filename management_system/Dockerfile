FROM python:3.8.3-alpine

WORKDIR /usr/src/app/
COPY Pipfile /usr/src/app
COPY Pipfile.lock /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /usr/src/app
WORKDIR /usr/src/app/management_system
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
