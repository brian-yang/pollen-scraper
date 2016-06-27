from scrapy.item import Item, Field

class PollenScraper(Item):
    title = Field()
    pollen_value = Field()
    severity = Field()
    top_allergens = Field()
