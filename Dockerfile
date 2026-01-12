# Setup dependencies
FROM python:3.11-slim-bullseye
RUN apt-get update && apt upgrade -y && \
    apt-get update && \
    apt-get install -y \
        git \
        curl \
        libcairo2 \
        libpango-1.0-0 \
        libgdk-pixbuf-2.0-0 \
        libffi-dev \
        shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Debian packages are way too old to be relied upon here
# hence turning to Python:
RUN pip install --upgrade pip pipenv

# Installing Python requirements
WORKDIR /opt/app

COPY requirements.txt ./

ENV PIPENV_VENV_IN_PROJECT=0
ENV PIPENV_SYSTEM=1

RUN pipenv lock
RUN pipenv install -r requirements.txt

COPY . .

# Fetching and installing Transifex client
RUN curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash

# Setting up and fetch translations the docs
RUN --mount=type=secret,id=tx_token,env=TX_TOKEN \
    ./tx add --project qfield-documentation --file-filter 'documentation/<project_slug>.<resource_slug>/<lang>.<ext>' remote https://app.transifex.com/opengisch/qfield-documentation/dashboard/ && \
    ./tx pull --minimum-perc 10

# Serving locally
CMD . /opt/app/.venv/bin/activate && mkdocs serve -a 0.0.0.0:8000
