import scrapy


class TestSpider(scrapy.Spider):
    name = "test2"
    # allowed_domains = [
    #     "www.naver.com",
    #     "www.daum.net",
    #     "www.zyte.com/blog/",
    # ]  # 크롤링이 허용된 도메인임 사실 이건 필수요소는 아님
    # start_urls = [
    #     "https://www.naver.com/",
    #     "https://www.daum.net",
    #     "https://www.zyte.com/blog/",
    # ]  # 멀티 도메인 :여러개 쓸수있음
    def start_requests(self):
        yield scrapy.Request("https://www.naver.com/", self.parse)
        yield scrapy.Request("https://www.daum.net", self.parse)
        yield scrapy.Request("https://www.zyte.com/blog/", self.parse)

    def parse(self, response):
        # print(response.url)
        self.logger.info("Response URL : {}".format(response.url))
        self.logger.info("Response STATUS : {}".format(response.status))

        if response.url.find("zyte"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
        elif response.url.find("naver"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
        elif response.url.find("daum"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
