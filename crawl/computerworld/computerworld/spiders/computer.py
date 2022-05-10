import scrapy


class ComputerSpider(scrapy.Spider):
    name = "computer"
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

        for idx, title in enumerate(titles):
            link = links[idx]
            img = imgs[idx]
            content = contents[idx]
            yield {"link": link, "title": title, "img": img, "content": content}
