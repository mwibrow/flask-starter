ARG PYTHON_ENV=production

FROM python:3.9-slim AS base
LABEL MAINTAINER "Mark Wibrow <m.wibrow@gmail.com>"

RUN apt-get -y update
RUN apt-get -y install build-essential \
    python3-dev \
    python3-pip
RUN pip install pipenv --upgrade

RUN adduser --system app
RUN mkdir -p /usr/src/app
RUN chown app /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/app/

FROM base AS build_production
ONBUILD RUN pipenv install --system

FROM base AS build_development
ONBUILD RUN pipenv install --dev --system

FROM build_${PYTHON_ENV}

COPY . /usr/src/app

USER app
