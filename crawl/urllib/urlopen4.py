import urllib.request as request
from urllib.error import HTTPError

# 다운로드 경로 및 파일명
path_list = ["d:/pthouse.jpg", "d:/naver.html"]

# 다운로드 받을 이미지 및 파일 지정
target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMjBfMjYy%2FMDAxNjEzNzk2NDc4NjMz.qZUFVDQ88JfAEAawEp3_tuZIVgmF-jWoOAG2MrsOHn4g.7CuAcsZYUdSiwyVTa0-1mkT3MMC-elIeSnPzJBVtTbgg.JPEG.hscw0402%2Foutput_3032638010.jpg&type=sc960_832",
    "http://www.naver.com",
]


#
for i, url in enumerate(target_url):  # 하나씩 꺼내오면서 번호를 붙여온다 i :번호 url: 첫번째 유알엘 정보
    try:
        response = request.urlopen(url)

        contents = response.read()
        print("*" * 50)
        print()
        print("Header info {} - {}".format(i, response.info()))
        print("Http Status Code {}".format(response.getcode()))
        print()
        print("*" * 50)

        # 파일저장

        with open(path_list[i], "wb") as f:  # 이미지는 wb임
            f.write(contents)

    except HTTPError as e:
        print(e)
    else:
        print("succeed")