import urllib.request as request

weather_url ="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

# 웹에서 가져온 정보를 메로리 위에 올려 작업하는 형태
data = request.urlopen(weather_url).read()

text = data.decode("utf-8") #euckr 사용할때도 있음

print(text[:4000]) # 0번부터 4000번까지 보여줘 !
