# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlexaprojectItem(scrapy.Item):
    # define the fields for your item here like:
    rank_num = scrapy.Field()

    site = scrapy.Field()

    staytime = scrapy.Field()

    page_view = scrapy.Field()
