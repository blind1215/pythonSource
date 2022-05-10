import urllib.request as request

api = "http://api.ipify.org"

url = api + "?" + "format=json"
print("요청 URL {}".format(url))

response = request.urlopen(url).read().decode("utf-8")

print(response)