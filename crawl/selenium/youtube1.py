# youtube 에 원하는 가수의 검색어를 넣고 결과 출력하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# webdriver 설정
driver = webdriver.Chrome("./driver/chromedriver")

# 원하는 페이지로 이동
driver.get("https://www.youtube.com/")

element = driver.find_element_by_name("search_query")
element.send_keys("아이유")
element.send_keys(Keys.ENTER)

# time.sleep(2)
driver.implicitly_wait(2)

titles = driver.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)