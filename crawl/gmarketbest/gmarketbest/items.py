# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GmarketbestItem(scrapy.Item):
    # define the fields for your item here like:
    main_cate = scrapy.Field()
    sub_cate = scrapy.Field()
    ranking = scrapy.Field()
    item_code = scrapy.Field()
    titles = scrapy.Field()
    o_price = scrapy.Field()
    s_price = scrapy.Field()
    sale_percent = scrapy.Field()
