import urllib.request as request
from urllib.error import HTTPError

try:
    url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"

    response = request.urlopen(url)
    contents = response.read().decode("euc-kr")
except HTTPError as e:
    print(e)
else:
    print("header info - {}".format(response.info()))
    print("content {}".format(contents[:3000]))