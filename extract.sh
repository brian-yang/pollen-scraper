#!/bin/bash

function usage() {
    echo "Usage: $0 -z <zipcode>" >&2
}

# Check if there are no options/arguments passed
if [ $# -eq 0 ];
then
    echo "No command line arguments found."
    usage
    exit 1
fi

while getopts ":z:" opt; do
    case $opt in
	z)
	    zip=$OPTARG
	    ;;
	\?)
	    echo "Invalid option: -$OPTARG." >&2
	    usage
	    exit 1
	    ;;
	:)
	    echo "Option -$OPTARG requires an argument." >&2
	    usage
	    exit 1
	    ;;
    esac
done
shift "$((OPTIND-1))"

echo "Scraping..."
scrapy crawl pollenscraper -a zipcode="$zip"
echo "Done scraping!"

echo "====================================="

echo "Enter PSQL password for user postgres."
sudo -u postgres psql -h localhost scrape << EOF
 CREATE TEMPORARY TABLE tempforecasts(tempid int);
 INSERT INTO tempforecasts(tempid) SELECT id FROM forecasts ORDER BY id DESC LIMIT 3;
 DELETE FROM forecasts WHERE NOT EXISTS (SELECT 1 FROM tempforecasts WHERE tempid = id);
 ALTER SEQUENCE public.forecasts_id_seq RESTART WITH 1;
 UPDATE forecasts SET id = DEFAULT;
 SELECT * FROM forecasts;
EOF

echo "If nothing is shown in the table, session timed out. Please try again."
