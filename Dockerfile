FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

# install dependencies

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY . /code/



