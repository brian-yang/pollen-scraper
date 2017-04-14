# pollen-scraper

## Supported Platforms ##
The pollen scraper can only run on:
* Mac OS X 10.9 Mavericks and 10.10 Yosemite
* Ubuntu Linux, Arch Linux, and other Unix-like operating systems

because dryscrape is only supported on these systems.

Here is more information about [dryscrape](https://github.com/niklasb/dryscrape/blob/master/README.md).

## Installing dependencies ##
You may want to create a python virtual environment before installing so as to not interfere with other python projects.
```bash
./setup.sh
```

### Setting up Postgres ###
**Ubuntu**
[Installation and basic server setup.](https://help.ubuntu.com/community/PostgreSQL)

**Mac**
[Installation and basic server setup.](http://postgresapp.com/)

### Dependencies/Installation pages ###
* [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html) (see platform specific installation notes first before installing)
* [Postgres](https://help.ubuntu.com/community/PostgreSQL)
* [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/intro.html) (installed in setup script)
* [dryscrape](http://dryscrape.readthedocs.io/en/latest/installation.html) (installed in setup script)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (install in setup script)
* xvfb (install in setup script or use apt-get)

## How to run ##
### Extract data ###
```bash
./extract.sh -z <zipcode>
```

## Additional Notes ##
Make sure that you rename the database_settings template to database_settings.py if you use it as database_settings.py has been added to the gitignore.
**PLEASE MAKE SURE THAT YOU DO NOT PUSH THE FILE WITH YOUR DATABASE SETTINGS!**

**Please ensure that Postgres is set up correctly, with a database named scrape and a user postgres.** The default database name can be changed in database_settings.py and the extract.sh script. The default user name can be changed in the extract.sh script.

**Also note that the crawler may time out sometimes without successfully extracting. The default timeout is 20 seconds, but this can be changed in pollen_spider.py.**

## Thank You Note ##
Special thanks to [newcoder](http://www.newcoder.io) for the amazing tutorial on web scraping!

## License ##
This product is licensed under the [MIT license](LICENSE) as well as the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/deed.en_US).