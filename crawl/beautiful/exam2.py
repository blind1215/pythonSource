# gmaket.co.kr 1차 카테고리 명 추출 =find_all()

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.gmarket.co.kr/")

soup = BeautifulSoup(r.text, "html.parser")

# print

categorys = soup.find_all("span", {"class": "link__1depth-item"})

for category in categorys:
    print(category)
    print(category.string)

# 2차 카테고리 가져오기

categorys2 = soup.find_all("a", {"class": "link__2depth-item"})

for category2 in categorys2:
    print(category2)
    print(category2.string)
