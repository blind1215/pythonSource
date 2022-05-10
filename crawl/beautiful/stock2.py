# https://finance.naver.com/ 인기검색종목의 이름과 가격 출력

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from fake_useragent import UserAgent

try:

    # 객체 생성
    userAgent = UserAgent()
    headers = {"user-agent": userAgent.chrome}

    url = "https://finance.naver.com/"

    with requests.Session() as s:
        s = requests.get(url, headers=headers)
        soup = BeautifulSoup(s.text, "html.parser")

except HTTPError as e:
    print(e)

# container > div.aside > div.group_aside > div.aside_area.aside_stock > table > tbody > tr:nth-child(1) > th
else:
    stocks = soup.select(
        "div.group_aside > div.aside_area.aside_stock > table > tbody > tr"
    )
    # print(stocks)

    for stock in stocks:
        stock_name = stock.select_one("th > a")
        stock_price = stock.find("td")
        print(stock_name.string, stock_price.string)
