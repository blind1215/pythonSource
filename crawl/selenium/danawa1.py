# 다나와 자동 로그인
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://www.danawa.com/")

driver.find_element_by_css_selector(".my_page_service > a").click()

userid = driver.find_element_by_id("danawa-member-login-input-id")
userid.clear()
userid.send_keys("pjky5")

userpw = driver.find_element_by_id("danawa-member-login-input-pwd")
userpw.clear()
userpw.send_keys("12344321@a")
userpw.send_keys(Keys.ENTER)
