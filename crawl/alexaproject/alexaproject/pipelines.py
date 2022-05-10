# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import openpyxl


class AlexaprojectPipeline:
    # def process_item(self, item, spider):
    #     if int(item["rank_num"]) < 41:
    #         return item
    #     else:
    #         raise DropItem("40위보다 아래임")

    # 초기화 메소드
    def __init__(self):  # 생성자 같은애임
        # 엑셀 처리 선언

        # 객체 생성
        self.workbook = openpyxl.Workbook()
        # 기본 시트 활성화
        self.worksheet = self.workbook.active
        # 너비 조정
        self.worksheet.column_dimensions["A"].width = 10
        self.worksheet.column_dimensions["B"].width = 15
        self.worksheet.column_dimensions["C"].width = 15
        self.worksheet.column_dimensions["D"].width = 20

        # 타이틀 행
        self.worksheet.append(["rank_num", "site", "staytime", "page_view"])

    def process_item(self, item, spider):
        if int(item["rank_num"]) < 41:

            # 엑셀저장
            rank_num = item["rank_num"]
            site = item["site"]
            staytime = item["staytime"]
            page_view = item["page_view"]

            self.worksheet.append([rank_num, site, staytime, page_view])

            return item
        else:
            raise DropItem("40위보다 아래임")

    # 마지막 1회 실행
    def close_spider(self, spider):
        self.workbook.save("./alexa.xlsx")
        self.workbook.close()
