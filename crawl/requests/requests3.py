import requests

s = requests.Session()

r = s.get("https://httpbin.org/cookies",cookies={"name":"hong"})

print(r.text)

s.close()