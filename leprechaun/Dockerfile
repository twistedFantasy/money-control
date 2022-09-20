FROM python:3.10.6
LABEL maintainer="Denis Sventitsky <denis.sventitsky@gmail.com> / Twisted Fantasy <twisteeed.fantasy@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/leprechaun/
RUN mkdir -p /usr/src/static/
WORKDIR /usr/src/leprechaun/

COPY leprechaun/ .
RUN pip --cache-dir=/usr/src/leprechaun/.pip-cache install -r requirements.txt
