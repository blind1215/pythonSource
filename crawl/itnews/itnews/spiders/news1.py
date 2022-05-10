import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# CrawlSpider : 연속적인 페이지 크롤링 할 때 사용
class News1Spider(CrawlSpider):  # 상속 CrawlSpider
    name = "news1"
    allowed_domains = ["news.daum.net"]
    start_urls = ["https://news.daum.net/breakingnews/digital"]

    # LinkExtractor : 링크 추출식
    rules = [
        Rule(
            LinkExtractor(allow=r"/breakingnews/digital\?page=\d$"),
            callback="parse_headline",
            follow=True,
        )
    ]

    # 스타트 유알엘이 던져주는거 받는곳
    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_headline(response)

    # rules는 headline이 받음
    def parse_headline(self, response):
        self.logger.info("parse_headline {}".format(response.url))

        # 헤드라인과 본문 가져오기
        headlines = response.css(
            "#mArticle > div.box_etc > ul > li > div > strong > a::text"
        ).getall()

        contents = response.css(
            "#mArticle > div.box_etc > ul > li > div > div > span::text"
        ).getall()

        for idx, headline in enumerate(headlines):
            yield {"headline": headline, "content": contents[idx].strip()}
