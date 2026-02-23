# Стадия сборки
FROM python:3.13-slim AS build

RUN apt update \
    && apt install -y unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock README.md /app/

WORKDIR /app

COPY src /app/src

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry build --format wheel \
    && pip install dist/*.whl \
    && rm -rf /root/.cache/pip

RUN mkdir -p /data

COPY deployment/entrypoints/*.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*.sh

WORKDIR /usr/local/lib/python3.13/site-packages/

FROM build AS final
