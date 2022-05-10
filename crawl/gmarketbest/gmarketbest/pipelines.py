# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class GmarketbestPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="biguser1",
            passwd="12345",
            database="bigdata",
            charset="utf8",
        )
        if self.conn:
            print("Connection 성공")
        else:
            print("Connection 실패")

        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Started")

        sql = """
            create table if not exists product(
                item_code varchar(20) not null primary key,
                titles varchar(200) not null,
                o_price int not null,
                s_price int not null,
                sale_percent int not null
            )
        """
        self.cursor.execute(sql)

        sql = """
            create table if not exists ranking(
                num int auto_increment not null primary key,
                main_category varchar(80) not null,
                sub_category varchar(80) not null,
                item_ranking tinyint unsigned not null,
                item_code varchar(20) not null
            )
        """
        self.cursor.execute(sql)
        # auto_increment > 시퀀스 같은 개념
        # tinyint  1byte만 쓰겠다 -128~127 임
        # unsigned 정수로 쓰겠다 -128~127 인데 정수만 쓰기로하니까 0~255

    def process_item(self, item, spider):

        sql = """
            insert into product(item_code,titles,o_price,s_price,sale_percent) values(%s,%s,%s,%s,%s)
        """
        values = (
            item.get("item_code"),
            item.get("titles"),
            item.get("o_price"),
            item.get("s_price"),
            int(item.get("sale_percent")),
        )

        self.cursor.execute(sql, values)

        sql = """
            insert into ranking(main_category,sub_category,item_ranking,item_code) values(%s,%s,%s,%s)
        """
        values = (
            item.get("main_cate"),
            item.get("sub_cate"),
            item.get("ranking"),
            item.get("item_code"),
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Stopped")
        self.conn.close()
