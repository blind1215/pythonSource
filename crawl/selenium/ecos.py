# 한눈에 보는 통계지표 다운로드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://ecos.bok.or.kr/EIndex.jsp")

# 100대 통계지표 클릭
driver.find_element_by_css_selector(".ESsubject_btn > li:nth-child(1) > a").click()

# 새창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(2)
# time.sleep(2)

# 새 창에서 엑셀 다운로드 클릭
driver.find_element_by_css_selector(".HScontent-header fieldset a").click()

time.sleep(2)