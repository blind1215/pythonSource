# https://news.v.daum.net/v/20210226111838232


# 뉴스 제목 출력

import requests  # 필요한거 가져올때
from bs4 import BeautifulSoup


r = requests.get("https://news.v.daum.net/v/20210226111838232")

soup = BeautifulSoup(r.text, "html.parser")

# print(soup)
news_title = soup.find("h3")
print(news_title)
print(news_title.string)

print()
# 기사 작성시간 출력하기
news_time = soup.find("span", class_="num_date")
print(news_time)
print(news_time.string)

print()
# 기사의 첫번째 문단 출력하기
paragraph = soup.find("p", {"dmcf-pid": "cOeD2HXtps"})
print(paragraph)
print(paragraph.string)

print()
# 기사 작성자 출력하기
writer = soup.find("span", class_="txt_info")
print(writer)
print(writer.string)
