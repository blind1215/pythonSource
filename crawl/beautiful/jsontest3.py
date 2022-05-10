import requests
import pprint

naver_open_news_api = "https://openapi.naver.com/v1/search/news.json"

param = {"query": "코로나", "sort": "sim", "display": 20}

header_params = {
    "X-Naver-Client-Id": "EYqAFT7GLD2L8fuTu3RF",
    "X-Naver-Client-Secret": "0_R7D9CeLm",
}

res = requests.get(naver_open_news_api, params=param, headers=header_params)

if res.status_code == 200:
    # print(res.json())
    # pprint.pprint(res.json()) # 이쁘게 출력
    data = res.json()
    # print(data["items"][0])
    # print()
    # pprint.pprint(data["items"][0])
    for idx, item in enumerate(data["items"], 1):
        print(idx, item["title"], item["link"])
else:
    print("Error code : ", res.status_code)
