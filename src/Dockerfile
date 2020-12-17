FROM tiangolo/meinheld-gunicorn-flask:python3.7
# https://github.com/tiangolo/meinheld-gunicorn-flask-docker

# Optionally, install some typical packages used for building and network debugging.
RUN apt-get update
RUN apt-get install -y  build-essential software-properties-common apt-transport-https build-essential ca-certificates netcat iputils-ping

# Update to the latest PIP
RUN pip3 install --upgrade pip

# Our application code will exist in the /app directory,
# so set the current working directory to that
WORKDIR /app

# Backup the default app files.  You could also delete these
# RUN mkdir bak && mv main.py uwsgi.ini bak

# Copy our files into the current working directory WORKDIR
COPY ./ ./

# install our dependencies
RUN pip3 install -r requirements.txt

# EXPOSE 5000