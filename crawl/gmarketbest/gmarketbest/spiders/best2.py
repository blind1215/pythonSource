import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from ..items import GmarketbestItem


class Best1Spider(scrapy.Spider):
    name = "best2"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]

    def parse(self, response):
        # 베스트 All 제품명 출력
        titles = response.css("div.best-list ul:not(.plus) > li > a::text").getall()

        # 판매 가격
        price = response.css("div.s-price span::text").getall()

        for idx, title in enumerate(titles):
            print("{}. {}. {}".format(idx + 1, title, price[idx]))
            # item = Gmarketproject2Item()
            # item["titles"] = title
            # item["price"] = int(price[idx].replace("원", "").replace(",", ""))
            # yield item
