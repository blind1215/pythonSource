import urllib.request as request
from urllib.error import HTTPError
from urllib.parse import urlparse

url = "http://www.encar.com/index.do"

try:
    response = request.urlopen(url)

    #수신 정보 확인
    print("type : {}".format(type(response)))
    print("getUrl : {}" .format(response.geturl()))
    print("status : {}".format(response.status))
    print("header : {}".format(response.getheaders()))
    print("getcode : {}".format(response.getcode()))


    # url 파싱
    print("parse : {}".format(urlparse("http://www.encar.com?test=test")))
    print("parse : {}".format(urlparse("http://www.encar.com?test=test").query))





    contents = response.read().decode("euc-kr")
except HTTPError as e:
    print(e)
else:
    print(contents[:4000])