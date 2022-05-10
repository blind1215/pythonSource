# 로그인 이후에 크롤링하기
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# 로그인 시 보내는 formData
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": "pjky5",
    "isSaveId": "true",
    "password": "12344321@a",
}
headers = {
    "user-agent": UserAgent().chrome,
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
}

with requests.Session() as s:
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    # print(res.text)

    # 로그인 후 주문/배송 조회 클릭하기
    res = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)
    # print(res.text)

    soup = BeautifulSoup(res.text, "html.parser")

    # 로그인 성공 체크
    check_id = soup.find("p", class_="user")

    if check_id is None:
        raise Exception("로그인 실패. 로그인 값 확인")

    # 출력문 형태
    #  ***** My Order Info *****
    #  입금대기 : 0
    #  결제완료 : 0
    #  배송중 : 0
    #  배송완료 : 0
    #  취소중 / 취소완료 : 0

    info_list = soup.select("div.sub_info > ul.info_list > li")
    # print(info_list)
    print("***** My Order Info *****")
    for item in info_list:
        proc, val = item.find("span").string, item.find("strong").string.strip()
        print("{} : {}".format(proc, val))
