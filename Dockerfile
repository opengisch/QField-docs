# Setup Python dependencies
FROM python:3.10-slim-bullseye
RUN apt-get update && apt upgrade -y && \
    apt install -y git curl && \
    # Debian packages are way too old to be relied upon here
    # hence turning to Python:
    pip install pipenv --upgrade pip

# Installing Python requirements
WORKDIR /opt/app
COPY . .
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --three

# Fetching and installing Transifex client
RUN curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash

# Token pass through for docker build --build-arg ...
ARG tx_token
ENV TX_TOKEN $tx_token

# Setting up and fetch translations the docs
RUN ./tx add --project qfield-documentation --file-filter 'documentation/<project_slug>.<resource_slug>/<lang>.<ext>' remote https://www.transifex.com/opengisch/qfield-documentation/dashboard/ && \
    ./tx pull --minimum-perc 10

# Serving locally
CMD . /opt/app/.venv/bin/activate && mkdocs serve -a 0.0.0.0:8000
