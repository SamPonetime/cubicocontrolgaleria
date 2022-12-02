# pull official base image
FROM python:3.11-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY django-insecure-xgnax-5393k$0er2+cxd9*3#f+r!78%elx@)3@$*7m7#+j-k*%

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y gcc

# copy project
COPY ./cubicoproject /usr/src/app/

# Upgrade packages
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r ./requeriments.txt
