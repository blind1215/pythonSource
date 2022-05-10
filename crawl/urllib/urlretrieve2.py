import urllib.request as request

# 정보를 가져올 url
html_url = "http://google.com"
# 이미지 가져오기
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMjFfMTgw%2FMDAxNTc0MzA0MDY0MTcw.NatvA6I4z22oenBNcgKk04cOQp3uEyCLh3lPf3nnLWUg.cI7kQzYyeeeiY3DplJ-tOUd08QRIPhYoKSinP8g_EEkg.JPEG.hanoiloh%2F463.jpg&type=sc960_832"

# 가져온 정보를 저장할 위치
save_url = "d:/google.html"
save_img = "d:/dog.png"
try:
    file1, header1 = request.urlretrieve(html_url, save_url)
    file2, header2 = request.urlretrieve(img_url, save_img)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")