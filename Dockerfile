FROM python:3.10-slim

# Install curl
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 
ENV \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adding poetry to PATH
ENV PATH $POETRY_HOME/bin:$PATH

# Create app directory
RUN mkdir /app
WORKDIR /app

# Copy needed files
COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry config virtualenvs.create false --local

# Install dependencies
RUN poetry install --no-root

# Copy rest of files
COPY . .

# Expose and start server
EXPOSE 8501
# CMD ["poetry", "run", "python", "main.py"]
