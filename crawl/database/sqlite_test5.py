# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결  : 현재는 테이블이 있기때문에 연결의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# 커서 획득
cursor = conn.cursor()

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

# sql
userList = (
    (3, "hong", "hong@naver.com", "hong.com", nowDateTime),
    (4, "cho", "cho@naver.com", "cho.com", nowDateTime),
    (5, "yoo", "yoo@naver.com", "yoo.com", nowDateTime),
)

sql = "insert into users values(?,?,?,?,?)"

cursor.executemany(sql, userList)
conn.commit()
conn.close()