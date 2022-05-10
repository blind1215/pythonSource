from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹 드라이버 로드
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://www.daum.net")

# 테스트 코드
assert "Daum" in driver.title


# 현재 접속한 사이트 소스 가져오기
# print(driver.page_source)

# 원하는 요소 찾기 - WebElement 리턴
search = driver.find_element(By.NAME, "q")
# 검색어 넣기
search.send_keys("안드로이드")
# 엔터 치기
search.send_keys(Keys.ENTER)
print(search)

driver.implicitly_wait(3)
