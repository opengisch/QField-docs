#   Setup a Python virtual environment
FROM python:3.9.13-slim-bullseye AS python-builder
RUN apt-get update && apt upgrade -y && pip install pipenv --upgrade pip
WORKDIR /opt/app
COPY ./requirements.txt .
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --three

#   Build the transifex-cli go static binary
FROM golang:1-bullseye AS go-builder
WORKDIR /opt/app
RUN git clone https://github.com/transifex/cli .

#   Fetch latest released version and build it from source
RUN git fetch --tags && latestTag=$(git describe --tags `git rev-list --tags --max-count=1`) && git checkout $latestTag
RUN make build

#   Gather the build artifacts
FROM python:3.9.13-slim-bullseye
WORKDIR /opt/app
COPY . .
COPY --from=python-builder /opt/app/.venv/ .venv/
COPY --from=go-builder /opt/app/bin/tx /bin/

#   Token pass through for docker build --build-arg ...
ARG tx_token
ENV TX_TOKEN $tx_token
ENV DEFAULT_LANGUAGE_ONLY false

#   Set up and fetch translations the docs
RUN tx add --project qfield-documentation --file-filter 'documentation/<project_slug>.<resource_slug>/<lang>.<ext>' remote https://www.transifex.com/opengisch/qfield-documentation/dashboard/ && \
    tx pull --minimum-perc 10

#   Serve locally
CMD . /opt/app/.venv/bin/activate && mkdocs serve -a 0.0.0.0:8000
