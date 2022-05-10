# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결  : 현재는 테이블이 있기때문에 연결의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# 커서 획득
cursor = conn.cursor()

# sql = "select * from users"

# cursor.execute(sql)

# fecth : 실행된 결과를 가져오는것
# fetchone(),fetchmany(), fetchall()
# print("first : ", cursor.fetchone())

# print("Three: ", cursor.fetchmany(size=3))  # 가지고온거 빼고 다음부터 size 만큼

# print("All : ", cursor.fetchall())

# for row in cursor.fetchall():
#     print(row)

for row in cursor.execute("select * from users order by id desc"):
    print(row)

conn.close()