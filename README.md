# pollen-scraper

## License ##
This product is licensed under the [MIT license](LICENSE) as well as the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/deed.en_US).

## Supported Platforms ##
The pollen scraper can only run on:
* Mac OS X 10.9 Mavericks and 10.10 Yosemite
* Ubuntu Linux, Arch Linux, and other Unix-like operating systems
because dryscrape is only supported on these systems.

Here is more information about [dryscrape](https://github.com/niklasb/dryscrape/blob/master/README.md).

## How to run ##

### Setup ###
You may want to create a python virtual environment before installing so as to not interfere with other python projects.
```bash
./setup.sh
```
*Postgres and scrapy should be set up independently.*

### Extract data ###
```bash
./extract.sh -z <zipcode>
```

## Dependencies/Installation pages ##
* [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html) (see platform specific installation notes first before installing)
* [Postgres](https://help.ubuntu.com/community/PostgreSQL)
* [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/intro.html) (installed in setup script)
* [dryscrape](http://dryscrape.readthedocs.io/en/latest/installation.html) (installed in setup script)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (install in setup script)

## Additional Notes ##
Please ensure that Postgres is set up correctly, with a database named scrape and a user postgres. The default database name can be changed in database_settings.py and the extract.sh script. The default user name can be changed in the extract.sh script.

Make sure that you rename the database_settings template to database_settings.py if you use it as database_settings.py has been added to the gitignore.
*Please make sure that you do not push the file with your database settings!*

Also note that the crawler may time out sometimes without successfully extracting. The default timeout is 20 seconds, but this can be changed in pollen_spider.py.