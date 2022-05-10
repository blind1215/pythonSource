# 구글 뉴스 (news.google.com)에서 뉴스를 검색하고
# 각 뉴스의 하이퍼링크를 수집하는 뉴스 클리핑 프로그램 구현

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main():
    # 요청
    url = "https://news.google.com/search?q=python&hl=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:

            res = s.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            news_clipping = data_extract(soup)

            for news_section in news_clipping:
                for k, v in news_section.items():
                    print("{} : {}".format(k, v))
                print()

    except HTTPError as e:
        print(e)


def data_extract(soup):
    # 뉴스 섹션 영역 가져오기
    # div > article
    section = soup.select("div.xrnccd > article")
    # print(section)

    # [{href:'https://google.com',title,'',},{},{},{}]
    news = []
    news_item = {}
    base_url = "https://news.google.com"

    # 링크, 제목, 내용,출처,등록일시
    for item in section:
        link_title = item.select_one("h3 > a")

        # 링크 주소
        # ./articles/CBMiJGh0dHBzOi8vd3d3LmNpb2tvcmVhLmNvbS9uZXdzLzE4NDU0N9IBAA?hl=ko&gl=KR&ceid=KR%3Ako
        # print(link_title["href"])
        # https://news.google.com/articles/CBMiJGh0dHBzOi8vd3d3LmNpb2tvcmVhLmNvbS9uZXdzLzE4NDU0N9IBAA?hl=ko&gl=KR&ceid=KR%3Ako
        news_item["href"] = base_url + link_title["href"][1:]
        # 제목 print(link_title.get_text())
        news_item["title"] = link_title.get_text()
        # 요약 내용 추출
        news_item["contents"] = item.select_one("div > span").get_text()
        # 작성일자,시간, 작성자
        report_time_date_writer = item.select_one("div.QmrVtf > div.SVJrMe")
        # 작성자 추출
        news_item["writer"] = report_time_date_writer.select_one("a").get_text()
        # 작성일자와 시간 추출 datetime="2021-02-26T01:54:15Z"
        report_date_time = report_time_date_writer.select_one("time")

        if report_date_time:
            report_date_time = report_date_time["datetime"].split("T")
            news_item["report_date"] = report_date_time[0]
            news_item["report_time"] = report_date_time[1]
        else:
            news_item["report_date"] = ""
            news_item["report_time"] = ""

        # 추출된 뉴스에 대한 정보 추가
        news.append(news_item)
        news_item = {}

    # 확인
    # print(news[:3])
    return news


if __name__ == "__main__":
    main()
