import scrapy
from ..items import MelonprojectItem


class MelonSpider(scrapy.Spider):
    name = "melon"
    allowed_domains = ["www.melon.com/chart/index.htm"]
    start_urls = ["https://www.melon.com/chart/index.htm"]

    def parse(self, response):
        # 제목
        titles = response.css(
            "#frm > div > table > tbody > tr > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a::text"
        ).getall()

        # 가수
        singers = response.xpath(
            "//*[@id='frm']/div/table/tbody/tr/td[4]/div/div/div[2]/a/text()"
        ).getall()

        # 앨범
        albums = response.xpath(
            "//*[@id='frm']/div/table/tbody/tr/td[5]/div/div/div/a/text()"
        ).getall()

        for idx, title in enumerate(titles):
            item = MelonprojectItem()
            item["titles"] = title
            item["singers"] = singers[idx]
            item["albums"] = albums[idx]

            yield item
