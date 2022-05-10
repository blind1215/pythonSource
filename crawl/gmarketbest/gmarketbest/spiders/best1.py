import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from ..items import GmarketbestItem


class Best1Spider(CrawlSpider):
    name = "best1"
    allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]

    rules = [
        Rule(
            LinkExtractor(allow=r"/Bestsellers\?viewType=G&groupCode=G(0|1)\d$"),
            callback="parse_sub_category",
        )
    ]

    def parse_start_url(self, response):
        print(">>>> parse_start_url ", response.url)
        yield scrapy.Request(
            response.url, self.parse_item, meta={"main_cate": "ALL", "sub_cate": "ALL"}
        )

    def parse_sub_category(self, response):

        # 1차 카테고리명 추출
        main_cate = response.css("div.gbest-cate ul li.on a::text").get()
        print(">>>>>>>>>{} {}".format(main_cate, response.url))

        # 1차 카테고리 best100 상품 출력
        yield scrapy.Request(
            response.url,
            self.parse_item,
            meta={"main_cate": main_cate, "sub_cate": main_cate},
            dont_filter=True,
        )

        # 2차 카테고리 추출-관련 상품군 제외
        sub_cate_addr = response.css(
            "div.navi ul li[class!='related'] a::attr('href')"
        ).getall()
        sub_cate_name = response.css(
            "div.navi ul li[class!='related'] a::text"
        ).getall()

        for idx, sub_addr in enumerate(sub_cate_addr):
            sub_url = response.urljoin(sub_addr)
            sub_name = sub_cate_name[idx]
            # print("2차 카테고리 ", sub_url, sub_name)
            # 2차 가테고리
            yield scrapy.Request(
                sub_url,
                self.parse_item,
                meta={"main_cate": main_cate, "sub_cate": sub_name},
                dont_filter=True,
            )

    def parse_item(self, response):
        # print(
        #     "parse_item {} , main_cate {} ,sub_cate {} ".format(
        #         response.url, response.meta["main_cate"], response.meta["sub_cate"]
        #     )
        # )

        # ALL : 200개 아이템 추출
        # 나머지 : 100 개 아이템 추출
        best_list = response.css(
            "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul:not(.plus) > li"
        )
        for idx, items in enumerate(best_list, 1):
            # 아이템 코드
            href = items.css("a::attr('href')").get()

            pattern = re.compile("code=[0-9]+")
            item_code = pattern.findall(href)[0].split("=")[1]

            # 제품명
            titles = items.css("a::text").get()
            # 원 가격
            o_price = items.css(
                "div.item_price > div.o-price > span > span::text"
            ).get()

            # 판매가격
            s_price = items.css(
                "div.item_price > div.s-price > strong > span > span::text"
            ).get()
            # 할인율
            sale = items.css("div.item_price > div.s-price > span > em::text").get()

            # 원 가격이 없는 경우
            if o_price == None:
                o_price = s_price

            # , 와 원 글자 지우기
            o_price = o_price.replace("원", "").replace(",", "")
            s_price = s_price.replace("원", "").replace(",", "")

            # 할인율이 없는 경우
            if sale == None:
                sale = "0"
            else:  # % 기호 제거
                sale = sale.replace("%", "")
            # print(
            #     "상품명 {} , 원가격 {} , 판매가격 {} , 할인율 {}".format(
            #         titles, o_price, s_price, sale
            #     )
            # )
            best_item = GmarketbestItem()
            best_item["ranking"] = idx
            best_item["main_cate"] = response.meta["main_cate"]
            best_item["sub_cate"] = response.meta["sub_cate"]
            best_item["item_code"] = item_code
            best_item["titles"] = titles
            best_item["o_price"] = o_price
            best_item["s_price"] = s_price
            best_item["sale_percent"] = sale
            yield best_item
