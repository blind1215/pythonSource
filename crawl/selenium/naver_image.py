from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time
import urllib.request as request
import os

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)  # time.sleep(3)

driver.get("https://www.naver.com")
driver.maximize_window()

# 검색어 입력하는 요소 찾기
element = driver.find_element_by_id("query")
# 검색어 입력
element.send_keys("트럭")
# 엔터
element.send_keys(Keys.ENTER)
# 전체 검색결과 페이지에서 이미지 탭 클릭
driver.find_element_by_css_selector("ul.base > li:nth-child(2) > a").click()

# img 가져오기
# main_pack > section > div._contentRoot.image_wrap > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb > a > img

# 이미지가 보여지는 영역의 태그 기다리기
img_tiles = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.photo_tile._grid"))
)

# 스크롤 이동
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2-200)")

time.sleep(5)

images = driver.find_elements_by_css_selector("div.thumb a img")

save_path = "d:\\imagedown\\"

idx = 1
for img in images:
    print(img.get_attribute("src"))
    file_name = os.path.join(save_path, save_path + str(idx) + ".png")
    request.urlretrieve(img.get_attribute("src"),file_name)
    idx +=1

time.sleep(2)