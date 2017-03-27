from scrapy.spiders import Spider
from scrapy.exceptions import CloseSpider
from scrapy.selector import Selector

# import sys
# sys.path.append("../..")
from scraper_app.items import PollenScraper

import dryscrape
from bs4 import BeautifulSoup

import os

class PollenSpider(Spider):
    name = 'pollenscraper'

    def __init__(self, date="", zipcode=""):
        self.allowed_domains = ['pollen.com']

        self.check_zipcode(zipcode)
        self.check_date(date)

        self.start_urls = ['http://pollen.com/forecast/current/pollen/' + self.zipcode]

        self.item_fields = {
            'title': ['h3', "day-header"],
            'pollen_value': ['p', "forecast-level"],
            'severity': ['p', "forecast-level-desc"]
        }

    def session_properties(self, sess):
        os.system("echo 'Setting properties...'")
        sess.set_attribute('auto_load_images', False) # do not load images
        sess.set_timeout(20) # set timeout

    def parse(self, response):
        # start session
        os.system("echo 'Starting xvfb instance...'")
        dryscrape.start_xvfb()
        session = dryscrape.Session() # start session
        self.session_properties(session)

        os.system("echo 'Crawling...'")

        # visit url
        session.visit(self.start_urls[0]) # visit website
        response = session.body()

        os.system("echo 'Done crawling.'")

        # pkill xvfb
        os.system("echo 'Closing xvfb instance (runs sudo pkill Xvfb)...'")
        os.system("sudo pkill Xvfb")

        # scraper objects
        self.scraper = PollenScraper()
        self.soup = BeautifulSoup(response, 'lxml')

        # extract
        if (self.date != ""):
            self.extract_date(self.date)

            # yield
            yield self.scraper

        else:
            for date in range(3):
                self.extract_date(date)

                # yield
                yield self.scraper

    def check_zipcode(self, z):
        if len(z) != 5 or not z.isdigit():
            raise CloseSpider('No zipcode given.')
        else:
            self.zipcode = z.strip()

    def check_date(self, d):
        try:
            if (d != ""):
                self.date = int(d)
            else:
                self.date = ""
        except:
            raise CloseSpider('Invalid date. date should either equal 0 (yesterday), 1 (today), or 2 (tomorrow).')

    def extract_date(self, d):
        for field, html in self.item_fields.iteritems():
            tags = str(self.soup.findAll(html[0], class_=html[1])[d])
            sel = Selector(text=tags)
            data = sel.xpath('//text()')
            extracted = data.extract()
            self.scraper[field] = extracted
