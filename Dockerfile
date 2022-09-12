#   Setup a Python virtual environment
FROM python:3.9.13-slim-bullseye AS python-builder
RUN apt-get update && apt upgrade -y && pip install pipenv --upgrade pip
WORKDIR /opt/app
COPY ./requirements.txt .
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --three

#   Build the transifex-cli go static binary
FROM golang:1-bullseye as go-builder
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
RUN tx add --project qfield-documentation --file-filter 'documentation/<project_slug>.<resource_slug>/<lang>.<ext>' remote https://www.transifex.com/opengisch/qfield-documentation/dashboard/ \
    && tx pull --all

#   Build the docs
CMD . .venv/bin/activate && mkdocs build

# To extract the build, run with a bindmount, for example:
#   mkdir site && docker run -it -v ./site:/opt/app/site --rm localhost/qfield-docs
# Then you can serve locally with your favorite web server, for example:
#   python3 -m http.server -d ./site
