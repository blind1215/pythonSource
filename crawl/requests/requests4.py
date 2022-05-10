import requests
from fake_useragent import UserAgent

s = requests.Session()

userAgent = UserAgent()

headers = {"user-agent": userAgent.chrom}

r = s.get("https://httpbin.org/get",headers=headers)

print(r.text)

s.close()