# 네이버 뉴스 가져오기

import urllib.request as request
from urllib.error import HTTPError
from fake_useragent import UserAgent

url = "https://news.v.daum.net/v/20210225104801527"
# url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=025&aid=0003080454"

try:
    userAgent = UserAgent()

    headers = {"User-agent": userAgent.chrome}

    request_url = request.Request(url, headers=headers)
    response = request.urlopen(request_url).read().decode("utf-8")

except HTTPError as e:
    print(e)
else:
    print(request_url.header_items())
    # print(resoponse)
