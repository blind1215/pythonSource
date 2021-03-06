# selenium + BeautifulSoup
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
driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 확인
# print(driver.page_source)

# 제조사별 더보기 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='dlMaker_simple']/dd/div[2]/button[1]")
    )
).click()

# 원하는 제조사 클릭  - 애플
# //*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='selectMaker_simple_priceCompare_A']/li[14]/label")
    )
).click()

time.sleep(5)

img_src, idx = "", 1

# 현재 페이지, 크롤링할 페이지 수
cur_page, target_crawl_num = 1, 6
try:
    while cur_page <= target_crawl_num:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup.prettify())

        product_list = soup.select("div.main_prodlist > ul > li:not(.product-pot)")
        # print(product_list)

        print("******* 현재 크롤링 페이지 : {}".format(cur_page))

        for product in product_list:
            # 상품명 출력
            if not product.find("div", class_="ad_header"):
                prod_name = product.select_one("p.prod_name > a").text.strip()
                prod_price = product.select_one("p.price_sect > a").text.strip()
                img = product.select_one(".thumb_image img")
                if img.get("data-original"):
                    img_src = img.get("data-original")
                else:
                    img_src = img.get("src")
                print(idx, prod_name, prod_price, "http:" + img_src)
                idx += 1
                # print(product.select_one("p.price_sect > a").text.strip())
        print()
        idx = 1

        # 현재 페이지 번호 변경
        cur_page += 1

        # 다음 페이지 번호 클릭하기
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(cur_page))
            )
        ).click()

        # soup 인스턴스 삭제
        del soup

        # 다음 페이지 요소들이 보여지는 시간 주기
        time.sleep(3)
except TimeoutException:
    print("**** 종료 *****")
time.sleep(3)

# productItem12660506 > div > div.prod_info > p > a
