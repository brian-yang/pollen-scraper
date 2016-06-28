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

    forecast_dates_xpath = '//div[@class="forecast-day"]'
    item_fields = {
        'title': './/div[@class="chart-col-wrapper"]/div[@class="chart-col"]/div[@class="no-padding"]/h3[@class="day-header"]/text()',
        'pollen_value': './/p[@class="forecast-level"]/text()',
        'severity': './/p[@class="forecast-level-desc"]/text()'
        #'top_allergens': '//span[@class="ng-binding"]/text()'
    }

    def parse(self, response):
        selector = Selector(response)
        log.msg("CHECKPOINT #1")
        log.msg(str(selector.xpath(self.forecast_dates_xpath)))

        for forecast in selector.xpath(self.forecast_dates_xpath):
            log.msg("CHECKPOINT #2")
            loader = ItemLoader(PollenScraper(), selector=forecast)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                log.msg("CHECKPOINT #3")
                loader.add_xpath(field, xpath)
                yield loader.load_item()
