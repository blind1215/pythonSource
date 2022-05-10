import scrapy


class MelonSpider(scrapy.Spider):
    name = "melon_a"
    allowed_domains = ["www.melon.com/chart/index.htm"]
    start_urls = ["https://www.melon.com/chart/index.htm"]

    def parse(self, response):
        # 선생님 ver
        # 곡명, 가수명, 앨범명 추출/파일저장
        songs = response.css("tbody > tr")
        idx = 0
        for song in songs:
            print(song)
            # 노래명
            title = song.css("td:nth-child(4) div.rank01 a::text").get()
            # 가수명
            singer = song.css("td:nth-child(4) div.rank02 a::text").get()
            # 앨범명
            album = song.css("td:nth-child(5) div.rank03 a::text").get()

            idx += 1

            yield {"idx": idx, "title": title, "singer": singer, "album": album}
