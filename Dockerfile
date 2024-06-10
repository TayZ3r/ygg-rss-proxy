FROM python:3.11-slim-bullseye

RUN pip install poetry
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN mkdir -p /tmp/flask_cache

ARG GUNICORN_PORT=8080
ENV EXPOSE_PORT=${GUNICORN_PORT}

EXPOSE ${EXPOSE_PORT}

CMD ["python", "-m", "ygg_rss_proxy"]
