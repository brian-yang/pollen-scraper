#!/bin/bash

echo "Installing Beautiful Soup, SQLAlchemy, and dryscrape..."

pip install beautifulsoup4
pip install sqlalchemy
pip install dryscrape

echo "Installing xvfb..."

sudo apt-get install xvfb

echo "Please install scrapy and set up Postgres separately."
