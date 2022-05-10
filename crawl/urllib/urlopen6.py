# 영화 진흥위원회

import urllib.request as request
from urllib.error import HTTPError


# 다운로드 받을 이미지 및 파일 지정
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20210224"

try:
    # file1, header1 = request.urlretrieve(url, "d:/movie.txt")
    data = request.urlopen(url).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    # print(header1)
    print("성공")
    print(data)
    with open("d:/movie.txt", "w") as f:
        f.write(data)