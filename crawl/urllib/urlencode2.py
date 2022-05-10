import urllib.request as request
from urllib.parse import urlencode

api = "http://api.ipify.org"

values = {"format":"json"}

url = api + "?" + urlencode(values)
print("before param :{}".format(values))
print("요청 URL {}".format(url))
print("after param : {}".format(urlencode(values)))

response = request.urlopen(url).read().decode("utf-8")

print(response)