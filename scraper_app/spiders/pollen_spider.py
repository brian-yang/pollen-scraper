from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.item import Item
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import PollenScraper

from scrapy import log

import dryscrape
from bs4 import BeautifulSoup

class PollenSpider(Spider):
    name = 'pollenscraper'

    allowed_domains = ['pollen.com']
    start_urls = ['http://pollen.com/forecast/current/pollen/90210']

    item_fields = {
        'title': ['h3', "day-header"],
        'pollen_value': ['p', "forecast-level"],
        'severity': ['p', "forecast-level-desc"]
    }

    def parse(self, response):
        # init
        session = dryscrape.Session()
        scraper = PollenScraper()
        session.visit(self.start_urls[0])
        response = session.body()
        soup = BeautifulSoup(response, 'lxml')
        
        # extract
        for field, html in self.item_fields.iteritems():
            tags = str(soup.find(html[0], class_=html[1]))
            sel = Selector(text=tags)
            data = sel.xpath('//text()')
            extracted = data.extract()
            scraper[field] = extracted
            log.msg(extracted)
        yield scraper
