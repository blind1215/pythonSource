import urllib.request as request

# 좋아하는 연예인 사진 가져오기
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F609%2F2020%2F12%2F15%2F202012150606031710_1_20201215060751380.jpg&type=sc960_832"


# 가져온 정보를 저장할 위치
save_img = "d:/kimso.png"
try:
    file2, header2 = request.urlretrieve(img_url, save_img)
except Exception as e:
    print(e)
else:
    print(header2)
    print("성공")