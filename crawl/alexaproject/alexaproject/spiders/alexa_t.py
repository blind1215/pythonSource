import scrapy
from ..items import AlexaprojectItem


class AlexaSpider(scrapy.Spider):
    name = "alexa_t"
    allowed_domains = ["www.alexa.com/topsites"]
    start_urls = ["https://www.alexa.com/topsites/"]

    def parse(self, response):
        for site in response.css("div.listings > div.site-listing").getall():
            # print(site)
            item = AlexaprojectItem()
            # 순위
            item["rank_num"] = site.css("").get()

            # 사이트명
            item["site"] = site.css("").get()

            # 머문시간
            item["staytime"] = site.css("").get()
            # 페이지 뷰
            item["page_view"] = site.css("").get()
            yield item
