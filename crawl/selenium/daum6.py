from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

# selenium => waits (time.sleep 으로 대체 가능)
# 웹 페이지에서 dom 의 element 들이 자리를 잡는 시간이 필요함
# 자리를 잡지 못할때 특정 엘리먼트를 찾으라고 하면 ElementNotVisibleException
# 발생 => waits 를 사용해서 이런 부분들을 해결함

# implicit wait : 요소를 찾기 위해 web driver가 일정 시간을 요청
# explicit wait : web driver이 실행을 계속하기 전에 특정 조건이 발생할 때까지
#                 기다리는 것

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("https://news.v.daum.net/v/20210305163153584")
driver.implicitly_wait(3)  # time.sleep(3)

loop, count = True, 0

while loop and count < 10:
    try:
        # 더보기 버튼 기다리기
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".cmt_box > div.alex_more > button")
            )
        )
        element.click()
        count += 1
    except TimeoutException:
        loop = False

# 댓글 내용 출력하기
# comment643556758
comments = driver.find_element_by_css_selector("dir.cmt_box ul.list_comment li")

for comment in comments:
    print(comment.text)
