import requests  # 필요한거 가져올때
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 네이버가 정보를 안주니 userAgent를 씀
userAgent = UserAgent()
headers = {"user-agent": userAgent.chrome}

r = requests.get(
    "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=014&aid=0004591241",
    headers=headers,
)

soup = BeautifulSoup(r.text, "html.parser")

# print(type(soup))

# print(soup)

# find() :제일 처음에 만나는 태그 가져오기
title = soup.find("h3", id="articleTitle")

print(title)
print(title.string)
print(title.get_text())