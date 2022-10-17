# Setup Python dependencies
FROM python:3.10-slim-bullseye
RUN apt-get update && apt upgrade -y && \
    apt install -y git curl

# Installing Python requirements
WORKDIR /opt/app
COPY . .
RUN pip3 install -r requirements.txt --upgrade pip

# Fetching and installing Transifex client
RUN curl -OL https://github.com/transifex/cli/releases/download/v1.3.1/tx-linux-amd64.tar.gz && \
    tar -xvzf tx-linux-amd64.tar.gz

# Preparing translations
RUN python3 ./utils/transifex_utils.py

# Token pass through for docker build --build-arg ...
ARG tx_token
ENV TX_TOKEN $tx_token

# Setting up and fetch translations the docs
RUN ./tx pull --translations --all --minimum-perc 10 && \
    ./tx status

CMD . /opt/app/.venv/bin/activate && python3 build-isolated.py
