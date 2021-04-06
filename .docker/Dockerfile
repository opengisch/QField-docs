FROM ubuntu:20.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-sphinx gettext python3-pip git

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
