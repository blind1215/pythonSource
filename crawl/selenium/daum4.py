# daum 접속 후 원하는 기사 클릭 후 이동
# 기사 상세보기에서 기사제목 출력하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("https://www.daum.net/")

driver.find_element_by_css_selector(".list_thumb > li:nth-child(2)").click()

print(driver.find_element_by_tag_name("h3").text)

time.sleep(2)
