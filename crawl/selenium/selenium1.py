# selenium
# 웹 테스트 프레임 워크
# 브라우저 자동화 = 브라우저를 조작하여 일을 시킬 수 있음
# 각 브라우저마다 웹 드라이버를 통해서 자동화 시킴
from selenium import webdriver
import time

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)  # 3초 정도 기다릴게

# 브라우저 크기
driver.maximize_window()

driver.get("http://www.naver.com")

print(driver.current_url)  # https://www.naver.com/
print(driver.title)  # NAVER

time.sleep(3)