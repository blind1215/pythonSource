# 수집 데이터를 일관성 있게 관리
# 데이터를 dict 구조로 관리
# 추후 가공 및 데이터베이스 저장 용이
# 자바에서 VO 개념과 비슷

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComputerworldItem(scrapy.Item):
    # define the fields for your item here like:

    # 제목
    title = scrapy.Field()
    # 이미지URL
    img = scrapy.Field()
    # 본문내용
    content = scrapy.Field()
    # 링크
    link = scrapy.Field()
