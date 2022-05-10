# 다음 뉴스 가져오기

import urllib.request as request
from urllib.error import HTTPError

try:
    url = "https://news.v.daum.net/v/20210225104801527"

    response = request.urlopen(url)
    contents = response.read().decode("utf-8")
except HTTPError as e:
    print(e)
else:
    print(response,contents)
    