from scrapy.spider import Spider
from scrapy.exceptions import CloseSpider
from scrapy.selector import Selector
from scrapy import log

from scraper_app.items import PollenScraper

import dryscrape
from bs4 import BeautifulSoup

import os, sys

class PollenSpider(Spider):
    name = 'pollenscraper'

    def __init__(self, date="", zipcode=""):
        self.allowed_domains = ['pollen.com']

        self.zipcode = zipcode.strip()
        
        if len(self.zipcode) != 5: # TODO: CHECK FOR VALID ZIPCODE
            raise CloseSpider('No zipcode given.')
        
        self.start_urls = ['http://pollen.com/forecast/current/pollen/' + self.zipcode]
        
        self.item_fields = {
            'title': ['h3', "day-header"],
            'pollen_value': ['p', "forecast-level"],
            'severity': ['p', "forecast-level-desc"]
        }

        try:
            if (date != ""):
                self.date = int(date)
            else:
                self.date = ""
        except:
            raise CloseSpider('Invalid date. date should either equal 0 (yesterday), 1 (today), or 2 (tomorrow).')

    def session_properties(self):
        log.msg("Setting properties...")
        self.session.set_attribute('auto_load_images', False) # do not load images
        self.session.set_timeout(20) # set timeout

    def parse(self, response):
        # start session
        dryscrape.start_xvfb()
        self.session = dryscrape.Session() # start session
        self.session_properties()
        
        log.msg("Scraping...")

        # visit url
        self.session.visit(self.start_urls[0]) # visit website
        response = self.session.body()

        # killall xvfb
        log.msg("Killing xvfb")
        os.system("sudo killall Xvfb")

        # scraper objects
        scraper = PollenScraper()
        self.soup = BeautifulSoup(response, 'lxml')
        
        # extract
        if (self.date != ""):
            for field, html in self.item_fields.iteritems():
                tags = str(self.soup.findAll(html[0], class_=html[1])[self.date])
                sel = Selector(text=tags)
                data = sel.xpath('//text()')
                extracted = data.extract()
                scraper[field] = extracted
                # log.msg(extracted)
            
            # yield
            yield scraper

        else:
            for date in range(3):
                for field, html in self.item_fields.iteritems():
                    tags = str(self.soup.findAll(html[0], class_=html[1])[date])
                    sel = Selector(text=tags)
                    data = sel.xpath('//text()')
                    extracted = data.extract()
                    scraper[field] = extracted
                    # log.msg(extracted)

                # yield
                yield scraper
