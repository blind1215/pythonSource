from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

headless_options = webdriver.ChromeOptions()
# 브라우저 안 띄우기
headless_options.add_argument("headless")

driver = webdriver.Chrome("./driver/chromedriver",options=headless_options)

driver.get("http://www.daum.net")

print("Session ID : {}".format(driver.session_id))  # 0e13bc1b85fe9ebe84f87bc1c6fd715c
print("Cookies : {}".format(driver.get_cookies))

# 검색어 넣고 엔터치기
element = driver.find_element_by_name("q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

# 추천검색어 가져오기
recomm_list = driver.find_elements_by_css_selector("#recomm_lists_top > span")

for recomm in recomm_list:
    print(recomm.text)


# 브라우저 뒤로 가기 클릭
# driver.back()  # driver.forward() : 앞으로 가기

time.sleep(3)
