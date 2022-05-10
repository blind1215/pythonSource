import requests
import pprint
import openpyxl
import re

# 엑셀 저장
excel_file = openpyxl.Workbook()
# 기본 시트 활성화
sheet1 = excel_file.active
# 컬럼 너비 변경
sheet1.column_dimensions["B"].width = 100
sheet1.column_dimensions["C"].width = 60
# 타이틀 행 지정
sheet1.append(["순위", "상품명", "주소"])
# 시트 명 지정
sheet1.title = "top1000"


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

            # item['title'] 태그 제거
            title = re.sub("<.+?>", "", item["title"])
            print(num, title, item["link"])
            sheet1.append([num, title, item["link"]])
    else:
        print("Error code : ", res.status_code)

excel_file.save("./crawl/data/top1000.xlsx")
excel_file.close()