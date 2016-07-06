from database_settings import *

BOT_NAME = 'pollenscraper'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = {'scraper_app.pipelines.PollenScraperPipeline': 1}

LOG_ENABLED = False
