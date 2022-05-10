import scrapy
from ..items import MelonprojectItem


class MelonSpider(scrapy.Spider):
    name = "melon2"
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


# 잘 되는거 같아요
# 아까 melon2 에 import 구문이 작성안되서 전체적으로 안 돌아갔나봐요
# 그러면 선생님 저아까 exel도 문제가 생기더라구요 그것도 이것때문에 그럴수있나요?
