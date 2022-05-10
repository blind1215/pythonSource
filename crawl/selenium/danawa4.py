# 다나와 로그인 + 제품명 검색 후 (옵션 선택..)
# 제품명 클릭 + 관심상품 담기 + 관심상품 리스트 출력하기

#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# 파싱을 위한 모듈
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)  # time.sleep(3)
driver.get("http://www.danawa.com/")

# 로그인 클릭해 danawa_header > div.danawa_top_search > div > div.my_service > div.my_service_list > ul > li.my_page_service > a > span
driver.find_element_by_css_selector(".my_page_service > a").click()

# 아이디넣기
userid = driver.find_element_by_id("danawa-member-login-input-id")
userid.clear()
userid.send_keys("blind1215")

# 패스워드넣기
userpw = driver.find_element_by_id("danawa-member-login-input-pwd")
userpw.clear()
userpw.send_keys("awd2648159@")
userpw.send_keys(Keys.ENTER)

time.sleep(3)

# 원하는 요소 찾기
search = driver.find_element(By.NAME, "k1")
search.send_keys("건조기")
# 엔터 치기
search.send_keys(Keys.ENTER)

time.sleep(3)

# 원하는 제조사 클릭
# //*[@id="SearchOption_Maker_Rep"]/div[1]/div/label/span[1]
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='SearchOption_Maker_Rep']/div[1]/div/label/span[1]")
    )
).click()

# 원하는 키로수 클릭
# //*[@id="SearchOption_BasicOption_93_All"]/div[2]/div/label/span
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='SearchOption_BasicOption_93_All']/div[2]/div/label/span")
    )
).click()

# 원하는 등급 클릭
# //*[@id="SearchOption_BasicOption_94_All"]/div[1]/div/label/span
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='SearchOption_BasicOption_94_All']/div[1]/div/label/span")
    )
).click()

time.sleep(3)

# 상품 클릭하기 #productItem13357328 > div > div.prod_info > p
# #productItem12113885 > div > div.prod_info > p > a
# #productItem12113885 > div > div.prod_info
driver.find_element_by_css_selector(
    "#productItem12113885 > div > div.prod_info > p > a"
).click()

# 새창으로 제어권
driver.switch_to.window(driver.window_handles[1])

time.sleep(4)


soup = BeautifulSoup(driver.page_source, "html.parser")

# 관심(하트에 해당하는 영역 가져오기
element = soup.select_one("#btn_bundle > ul >li.item.interest")

# 관심 상품 넣기
# //*[@id="wishFolder_101905482"]
# #interest
# //*[@id="wishFolder_101905482"] //*[@id="wishFolder_101905482"]
if "on" not in element["class"]:
    # 관심클릭
    driver.find_element_by_css_selector("#interest").click()
    # 저장할 폴더클릭
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='wishFolder_101905482']"))
    ).click()

time.sleep(3)

del soup

# 관심상품리스트로 가기
# //*[@id="danawa_header"]/div[2]/div/div[3]/div[1]/ul/li[2]/a/span[1]
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[@id='danawa_header']/div[2]/div/div[3]/div[1]/ul/li[2]/a/span[1]",
        )
    )
).click()

time.sleep(3)

# 상세 페이지
soup = BeautifulSoup(driver.page_source, "html.parser")

wishlist = soup.select("table.wish_tbl > tbody >tr")

for idx, item in enumerate(wishlist, 1):
    product_name = item.select_one("td.info > div.tit > a").text
    product_spec = item.select_one("dl.spec > dd >a").text
    product_price = item.select_one("td.lowest > dl >dd >span").text

    print("[{}] {}".format(idx, product_name))
    print("[{}] {}".format(idx, product_spec))
    print("[{}] {}".format(idx, product_price))
print()