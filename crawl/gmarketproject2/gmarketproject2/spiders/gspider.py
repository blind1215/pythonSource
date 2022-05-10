import scrapy
from ..items import Gmarketproject2Item


class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["https://corners.gmarket.co.kr/Bestsellers/"]

    def parse(self, response):
        # 베스트 All 제품명 출력
        titles = response.css("div.best-list ul:not(.plus) > li > a::text").getall()

        # 판매 가격
        price = response.css("div.s-price span::text").getall()

        for idx, title in enumerate(titles):
            # print("{}. {}. {}".format(idx + 1, title, price[idx]))
            item = Gmarketproject2Item()
            item["titles"] = title
            item["price"] = int(price[idx].replace("원", "").replace(",", ""))
            yield item
