import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ItnewsItem

# CrawlSpider : 연속적인 페이지 크롤링 할 때 사용
class News1Spider(CrawlSpider):  # 상속 CrawlSpider
    name = "news2"
    allowed_domains = ["news.daum.net"]
    start_urls = ["https://news.daum.net/breakingnews/society"]

    # LinkExtractor : 링크 추출식
    rules = [
        Rule(
            LinkExtractor(allow=r"/breakingnews/society\?page=\d$"),
            callback="parse_parent",
            follow=True,
        )
    ]

    # 스타트 유알엘이 던져주는거 받는곳
    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_parent(response)

    def parse_parent(self, response):
        # self.logger.info("Parent Response URL : {}".format(response.url))

        # 링크 추출
        urls = response.css(
            "#mArticle > div.box_etc > ul > li > div > strong > a::attr('href')"
        ).getall()

        for url in urls:
            yield scrapy.Request(
                url,
                self.parse_child,
                meta={"parent_link": response.url},
                dont_filter=True,
            )

    # rules는 headline이 받음
    def parse_child(self, response):
        # self.logger.info(
        #     "Response From Parent URL {}".format(response.meta["parent_link"])
        # )
        # self.logger.info("Child URL {}".format(response.url))

        # 상세기사에서 기사 제목과 내용을 추출
        # 아이템 담기(부모주소,상세기사주소,기사제목,내용)

        # 기사 제목
        headline = response.css("#cSub > div > h3::text").get()
        # 내용
        contents = response.css("#harmonyContainer > section > p::text").getall()
        contents = "".join(contents).strip()

        # 아이템
        item = ItnewsItem()
        item["parent_link"] = response.meta["parent_link"]
        item["headline"] = headline
        item["article_link"] = response.url
        item["contents"] = contents
        yield item
