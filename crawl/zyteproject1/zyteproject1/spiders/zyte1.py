import scrapy


class Zyte1Spider(scrapy.Spider):
    name = "zyte1"
    allowed_domains = ["www.zyte.com/blog/"]
    start_urls = ["https://www.zyte.com/blog/"]

    def parse(self, response):  # 리스폰스에 담겨서 호출됨
        # print(response.text)
        print("response.url : {}".format(response.url))  # response의 url을 보여줌
        print("dir : {}".format(dir(response)))  # response가 쓸수있는 함수
        print("status : {}".format(response.status))  # 현재 상태 200 인지 400인지
        print("body : {}".format(response.body))  # byte 형태로 나옴
