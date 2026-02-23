# Стадия сборки
FROM python:3.13-slim as build
ENV USERNAME=app

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

RUN groupadd -g 999 $USERNAME \
    && useradd -u 999 -g 999 -s /sbin/nologin -c "Docker image user" $USERNAME \
    && mkdir -p /data \
    && chown -R 999:999 /data \
    && chmod -R 750 /data

COPY --chown=app:app deployment/entrypoints/*.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*.sh

WORKDIR /usr/local/lib/python3.13/site-packages/

USER $USERNAME

FROM build as final
