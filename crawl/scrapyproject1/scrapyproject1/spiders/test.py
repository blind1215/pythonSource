import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    # allowed_domains = [
    #     "www.naver.com",
    #     "www.daum.net",
    #     "www.zyte.com",
    # ]  # 크롤링이 허용된 도메인임 / 어떤도메인을 허용할것인지 /필수요소는 아님
    start_urls = [
        "https://www.naver.com/",
        "https://www.daum.net",
        "https://www.zyte.com/blog/",
    ]  # 멀티 도메인 :여러개 쓸수있음

    def parse(self, response):
        yield scrapy.Request(response.url, self.parse_title)  # 좀전에 받은 url 요청할거야

    def parse_title(self, response):
        print(response.css("head > title::text").get())
