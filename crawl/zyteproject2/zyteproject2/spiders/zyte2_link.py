import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2_link"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["https://www.zyte.com/blog/"]

    # def parse(self, response):
    #     # 타이틀 추출하기 #_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > div > a
    #     title = response.scc(
    #         "#_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > div > a::text"
    #     ).get()
    #     # 작성날짜 추출하기 #_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > a > div.oxy-post-image-date-overlay
    #     date = (
    #         response.css(
    #             "#_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > a > div.oxy-post-image-date-overlay::text"
    #         )
    #         .get()
    #         .strip()
    #     )
    #     # 링크 추출하기
    #     link = response.css(
    #         "#_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > div > a::attr('href')"
    #     ).get()

    #     print(title, date, link)
    def parse(self, response):

        for url in response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::attr('href')"
        ).getall():

            # urljoin : 재귀호출 시 상대경로로 되어 있는 주소를 절대 경로로 변경
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_article)

    def parse_article(self, response):
        print(response.url)

        contents = response.css("#blog-body span p::text").extract_first()
        # print(contents)
        yield {"contents": contents}
