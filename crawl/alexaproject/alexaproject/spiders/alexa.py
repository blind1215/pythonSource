import scrapy
from ..items import AlexaprojectItem


class AlexaSpider(scrapy.Spider):
    name = "alexa"
    allowed_domains = ["www.alexa.com/topsites"]
    start_urls = ["https://www.alexa.com/topsites/"]

    def parse(self, response):
        # 순위
        rank_nums = response.css("div.site-listing > div:nth-child(1)::text").getall()
        # 사이트명
        sites = response.css(
            "div.site-listing > div.td.DescriptionCell > p > a::text"
        ).getall()
        # 머문시간
        staytimes = response.css(
            "div.site-listing > div:nth-child(3) > p::text"
        ).getall()
        # 페이지 뷰
        page_views = response.css(
            "div.site-listing > div:nth-child(4) > p::text"
        ).getall()

        for idx, rank_num in enumerate(rank_nums):
            # print(
            #     "{}. {}. {} . {}".format(
            #         rank_num, sites[idx], staytimes[idx], page_views[idx]
            #     )
            # )
            item = AlexaprojectItem()
            item["rank_num"] = int(rank_num)

            # 사이트명
            item["site"] = sites[idx]

            # 머문시간
            item["staytime"] = staytimes[idx]
            # 페이지 뷰
            item["page_view"] = page_views[idx]
            yield item
