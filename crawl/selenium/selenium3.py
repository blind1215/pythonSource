from selenium import webdriver

# webdriver 설정
driver = webdriver.Chrome("./driver/chromedriver")

# 원하는 페이지로 이동
driver.get("http://python.org")

# 타이틀 출력  Welcome to Python.org
print(driver.title)

# 테스트 코드
assert "Python" in driver.title


# 전체소스 가져오기
print(driver.page_source)