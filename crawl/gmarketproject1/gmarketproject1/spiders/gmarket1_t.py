import scrapy
from scrapy_selenium import SeleniumRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1_t"
    # allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G11"]

    def parse(self, response):
        urls = response.css(
            "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > a::attr('href')"
        ).getall()

        for url in urls:
            # yield scrapy.Request(url, self.parse_article)
            yield SeleniumRequest(
                url=url,
                callback=self.parse_url,
                wait_time=5,
                wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, "h1.itemtit")),
            )

    def parse_url(self, response):
        # print(response.url)
        # 상품명
        title = response.css("h1.itemtit::text").get()

        yield {"여행 url": response.url, "상품명": title}
