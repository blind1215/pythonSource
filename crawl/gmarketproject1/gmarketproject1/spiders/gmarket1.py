import scrapy


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]

    def parse(self, response):  # ajax에선 success가 있어야 실행되는데 parse는 알아서 해줌
        # 베스트 All 제품명 출력
        titles = response.css("div.best-list ul:not(.plus) > li > a::text").getall()

        # 판매 가격
        price = response.css("div.s-price span::text").getall()

        for idx, title in enumerate(titles):
            print("{}. {}. {}".format(idx + 1, title, price[idx]))
