#!/bin/bash

function usage() {
    echo "Usage: $0 -z {zipcode}" >&2
}

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

echo "Please enter the password for user: postgres."
sudo -u postgres psql -h localhost scrape >/dev/null << EOF
 DELETE FROM forecasts;
 ALTER SEQUENCE public.forecasts_id_seq RESTART WITH 1;
EOF

echo "Scraping..."
scrapy crawl pollenscraper -a zipcode="$zip"
echo "Done scraping!"

echo "Please enter again the password for user: postgres."
sudo -u postgres psql -h localhost scrape << EOF
 SELECT * FROM forecasts;
EOF

echo "If nothing is shown in the table, session timed out. Please try again."
