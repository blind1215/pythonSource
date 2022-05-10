import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com/tag/humor"]
    start_urls = ["http://quotes.toscrape.com/tag/humor/"]

    # 기본으로 만들어진 메소드임
    def parse(self, response):  # 응답에서
        for quote in response.css("div.quote"):  # css로 된거 찾아와
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }
        next_page = response.css("li.next a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)  # 재귀호출:자기자신을 부름
