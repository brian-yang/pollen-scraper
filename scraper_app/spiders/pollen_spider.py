from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import PollenScraper

class PollenSpider(Spider):
    name = 'pollenscraper'

    allowed_domains = ['pollen.com']
    start_urls = ['http://pollen.com/forecast/current/pollen/90210']

    forecast_dates_xpath = '//div[@class="forecast-day ng-scope ng-isolate-scope"]'
    item_fields = {'title': './/h3[@class="day-header ng-binding"]/text()',
                   'pollen_value': './/p[@class="forecast-level ng-binding"]/text()',
                   'severity': '//p[@class="forecast-level-desc ng-binding"]/text()',
                   'top_allergens': '//span[@class="ng-binding"]/text()'}

    def parse(self, response):
        selector = Selector(response)

        for forecast in selector.xpath(self.forecast_dates_xpath):
            loader = XPathItemLoader(PollenScraper(), selector=forecast)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
                yield loader.load_item()
