# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MelonprojectItem(scrapy.Item):
    # define the fields for your item here like:
    titles = scrapy.Field()
    singers = scrapy.Field()
    albums = scrapy.Field()
