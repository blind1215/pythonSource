import scrapy
from ..items import ComputerworldItem

# 아이템 사용


class ComputerSpider(scrapy.Spider):
    name = "computer2"
    allowed_domains = ["https://www.computerworld.com/news"]
    start_urls = ["https://www.computerworld.com/news/"]

    def parse(self, response):
        # 세부기사 링크 가져오기
        links = response.css("div.post-cont h3 a::attr('href')").getall()
        # 타이틀 모두 가져오기
        titles = response.css("div.post-cont h3 a::text").getall()
        # 이미지 전체 주소 가져오기
        imgs = response.css("figure.well-img > a > img::attr('data-original')").getall()
        # 간단 내용 가져오기
        contents = response.css("div.post-cont h4::text").getall()

        # 아이템으로 저장할 수 있는 코드 추가
        for idx, title in enumerate(titles):
            item = ComputerworldItem()

            item["link"] = links[idx]
            item["img"] = imgs[idx]
            item["content"] = contents[idx]
            item["title"] = title
            yield item
