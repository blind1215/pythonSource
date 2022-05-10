import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2_xpath"
    allowed_domains = ["www.zyte.com/blog"]
    start_urls = ["https://www.zyte.com/blog/"]

    # def parse(self, response):
    #     # 타이틀 추출하기
    #     title = response.xpath(
    #         "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/div[2]/div/a/text()"
    #     ).extract_first()
    #     # 작성날짜 추출하기
    #     date = (
    #         response.xpath(
    #             "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/a/div[2]/text()"
    #         )
    #         .extract_first()
    #         .strip()
    #     )
    #     # 링크 추출하기
    #     link = response.xpath(
    #         "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/div[2]/div/a/@href"
    #     ).extract_first()

    #     print(title, date, link)

    def parse(self, response):
        # 타이틀 추출하기
        titles = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/div[2]/div/a/text()"
        ).extract()
        # 작성날짜 추출하기
        dates = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/a/div[2]/text()"
        ).extract()
        # 링크 추출하기
        links = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/div[2]/div/a/@href"
        ).extract()

        # print("타이틀 :{}".format(titles))
        # print("날짜 :{}".format(dates))
        # print("링크 :{}".format(links))

        for idx, title in enumerate(titles):
            # print("{} {} {}".format(dates[idx].strip(), title, links[idx]))

            # yield== 리턴 : Request,Item,Dictionary,None
            yield {"date": dates[idx].strip(), "title": title, "link": links[idx]}
