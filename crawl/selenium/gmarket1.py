from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("https://www.gmarket.co.kr/")

element = driver.find_element_by_name("keyword")
element.send_keys("운동화")
element.send_keys(Keys.ENTER)
