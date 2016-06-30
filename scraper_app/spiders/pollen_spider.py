from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import PollenScraper

# For debugging
from scrapy import log

class PollenSpider(Spider):
    name = 'pollenscraper'

    allowed_domains = ['pollen.com']
    start_urls = ['http://pollen.com/forecast/current/pollen/90210']

    forecast_dates_xpath = '//script[@id="/forecast/day.html"]'
    item_fields = {
        'title': './/text()',
        #'pollen_value': './/p[text()]',
        #'severity': './/p[@class="forecast-level-desc"][text()]'
        #'top_allergens': '//span[@class="ng-binding"]/text()'
    }

    def parse_item(self, response):
        pass
