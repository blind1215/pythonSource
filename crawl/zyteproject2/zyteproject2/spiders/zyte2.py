import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2"
    allowed_domains = ["www.zyte.com/blog"]
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
        # 현재 페이지의 모든 타이틀 추출
        titles = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::text"
        ).getall()
        # 현재 페이지의 모든 날짜 추출
        dates = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > a > div.oxy-post-image-date-overlay::text"
        ).getall()

        # 현재페이지의 모든 링크 추출
        links = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::attr('href')"
        ).getall()

        # print("타이틀 :{}".format(titles))
        # print("날짜 :{}".format(dates))
        # print("링크 :{}".format(links))

        for idx, title in enumerate(titles):
            # print("{} {} {}".format(dates[idx].strip(), title, links[idx]))

            # 리턴 : Request,Item,Dictionary,None
            yield {"date": dates[idx].strip(), "title": title, "link": links[idx]}
