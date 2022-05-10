from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://www.daum.net")

print("Session ID : {}".format(driver.session_id))  # 0e13bc1b85fe9ebe84f87bc1c6fd715c
print("Cookies : {}".format(driver.get_cookies))

# 검색어 넣고 엔터치기
element = driver.find_element_by_name("q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

# 브라우저 뒤로 가기 클릭
driver.back()  # driver.forward() : 앞으로 가기

time.sleep(3)
