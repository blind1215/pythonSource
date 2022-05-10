# clien 사이트의 팁과 강좌 게시판의 1~5 페이지의 타이틀 가져오기

# 1page:https://www.clien.net/service/board/lecture
# 1page:https://www.clien.net/service/board/lecture?&od=T31&po=0
# 2page:https://www.clien.net/service/board/lecture?&od=T31&po=1
# 3page:https://www.clien.net/service/board/lecture?&od=T31&po=2
# 5page:https://www.clien.net/service/board/lecture?&od=T31&po=4

import requests
from bs4 import BeautifulSoup

for page_num in range(5):
    if page_num == 0:  # 1page 요청
        r = requests.get("https://www.clien.net/service/board/lecture")
    else:
        r = requests.get(
            "https://www.clien.net/service/board/lecture?&od=T31&po=" + str(page_num)
        )

    # 게시판의 타이틀 출력

    soup = BeautifulSoup(r.text, "html.parser")

    # div_content > div.list_content > div:nth-child(1) > div.list_title > a.list_subject > span.subject_fixed
    # div_content > div.list_content > div:nth-child(24) > div.list_title > a.list_subject > span.subject_fixed
    # 타이틀 가져오기

    titles = soup.select("span.subject_fixed")
    # print(titles)

    for item in titles:
        print(item.text.strip())
    print()
