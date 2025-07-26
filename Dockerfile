FROM python:3.12.11-slim-bullseye AS base

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="kpa.settings"
ENV POETRY_HOME="/poetry"
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="/poetry/bin:$PATH"

WORKDIR /kpa-backend

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN addgroup --gid $GROUP_ID appgroup && \
  adduser --uid $USER_ID --gid $GROUP_ID --disabled-password --gecos '' appuser

# Install system deps
RUN apt-get update && apt-get install -y curl make

# Install poetry as root
RUN curl -sSL https://install.python-poetry.org | python3 - && \
  chown -R appuser:appgroup $POETRY_HOME

# Prepare working dir
RUN mkdir -p /kpa-backend && chown -R appuser:appgroup /kpa-backend

# Copy files and switch user
COPY ./pyproject.toml ./poetry.lock ./

USER appuser

# Development Image
FROM base AS dev

RUN poetry sync --all-groups
COPY . .

CMD ["make", "runserver"]

