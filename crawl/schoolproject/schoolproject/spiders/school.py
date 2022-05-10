import scrapy


class SchoolSpider(scrapy.Spider):
    name = "school"
    allowed_domains = ["w3schools.com"]
    start_urls = ["https://w3schools.com/"]

    def parse(self, response):
        # 강좌목록
        lectures = response.css("#mySidenav > div > a::text").getall()
        # 링크주소
        links = response.css("#mySidenav > div > a::attr('href')").getall()

        for idx, lecture in enumerate(lectures):
            yield {"title": lecture, "link": links[idx]}
