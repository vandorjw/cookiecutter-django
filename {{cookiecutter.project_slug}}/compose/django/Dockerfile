FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV PIPENV_MAX_DEPTH 1
ENV PIPENV_VENV_IN_PROJECT True

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # CFFI dependencies
  && apk add libffi-dev openssl-dev py-cffi

RUN useradd -c 'pyuser' --home-dir /app -s /bin/bash pyuser
RUN echo 'pyuser:pyuser' | chpasswd

RUN pip install pipenv

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN cd /app && pipenv install

COPY ./compose/django/gunicorn.sh /gunicorn.sh
RUN chmod a+x /gunicorn.sh
RUN chown pyuser /gunicorn.sh

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
RUN chown pyuser /entrypoint.sh

COPY ./compose/django/celery/worker/start.sh /start-celeryworker.sh
RUN chmod a+x /start-celeryworker.sh
RUN chown pyuser /start-celeryworker.sh

COPY ./src /app/src

RUN chown -R pyuser /app

USER pyuser

WORKDIR /app/src

EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
