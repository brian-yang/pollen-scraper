#!/bin/bash

echo "Installing scrapy, Beautiful Soup, SQLAlchemy, dryscrape..."

pip install scrapy
pip install beautifulsoup4
pip install sqlalchemy
pip install dryscrape

echo "Installing xvfb..."

sudo apt-get install xvfb

echo "Please set up Postgres separately. See the README for more details."
echo "Once you've set up Postgres, please enter your Postgres username and password in database_settings.py."
