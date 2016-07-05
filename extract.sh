#!/bin/bash

sudo -u postgres psql -h localhost scrape << EOF
 DELETE FROM forecasts;
 ALTER SEQUENCE public.forecasts_id_seq RESTART WITH 1;
 UPDATE forecasts SET id = DEFAULT;
EOF

scrapy crawl pollenscraper -a zipcode=90210

sudo -u postgres psql -h localhost scrape << EOF
 SELECT * FROM forecasts;
EOF
