#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install python3-pip python3-venv

# install postgres and setup user and db
sudo apt-get -y install postgresql postgresql-contrib
(cd /home/ubuntu/app; sudo -u postgres psql -f fixtures.sql)

(cd /home/ubuntu/app; python3 -m venv .env)
(cd /home/ubuntu/app; .env/bin/pip install --upgrade pip)
(cd /home/ubuntu/app; .env/bin/pip install -r requirements.txt)
(cd /home/ubuntu/app; .env/bin/python manage.py db upgrade)
