# https://ko.wikipedia.org/wiki/서울_지하철

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:

    url = "https://ko.wikipedia.org/wiki/서울_지하철"

    with requests.Session() as s:
        # get(),soup 객체 생성
        r = s.get(url)
        soup = BeautifulSoup(r.text, "html.parser")


except HTTPError as e:
    print(e)

else:
    # 첫번째 이미지 가져오기
    image1 = soup.select_one("img")
    print(image1)

    print()
    # 두번째 이미지 가져오기
    image2 = soup.select_one("img.thumbimage")
    print(image2)

    print()
    # 첫번째 이미지 src 출력
    print(image1["src"])
    # 두번째 이미지 src 출력
    print(image2["src"])