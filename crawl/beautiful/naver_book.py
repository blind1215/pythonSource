# 네이버의 open api 검색 부분 중 도서 정보 가져오기
# 출력결과
# 번호 isbn 제목 가격 할인가격

import requests
import pprint

header_params = {
    "X-Naver-Client-Id": "d4RzEF7WYoi2xGZGRohH",
    "X-Naver-Client-Secret": "06bo6v60Jz",
}
book_api = "https://openapi.naver.com/v1/search/book.json"

start, num = 1, 1
for idx in range(3):

    start_num = start + (idx * 100)

    param = {"query": "정보처리기사", "display": 100, "start": start_num}

    res = requests.get(book_api, params=param, headers=header_params)

    data = res.json()
    for item in data["items"]:
        print(num, item["isbn"], item["title"], item["price"], item["discount"])
        num += 1
