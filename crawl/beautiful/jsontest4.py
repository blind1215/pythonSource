import requests
import pprint


# https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=1
# https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=101
# https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=201


header_params = {
    "X-Naver-Client-Id": "EYqAFT7GLD2L8fuTu3RF",
    "X-Naver-Client-Secret": "0_R7D9CeLm",
}
shop_api = "https://openapi.naver.com/v1/search/shop.json"

start, num = 1, 0
for idx in range(10):

    start_num = start + (idx * 100)
    param = {"query": "아이폰", "start": str(start_num), "display": 100}
    # print(shop_api)

    res = requests.get(shop_api, params=param, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        for item in data["items"]:
            num += 1
            print(num, item["title"], item["link"])
    else:
        print("Error code : ", res.status_code)
