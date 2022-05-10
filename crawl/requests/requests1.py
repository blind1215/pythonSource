import requests

# requests
# 세션을 이용한 접속
# 4가지 메소드(get,post,delete,put) 사용 가능
# 디코딩도 적절하게 작업해 줌
# 가져오는 데이터에 대해서 json 처리도 편함

# 세션 활성화
s = requests.Session()
r = s.get("https://www.naver.com")

# print(r.text)
print("status code : {}".format(r.status_code))
print("OK? :{}".format(r.ok))


# 세션 종료
s.close()