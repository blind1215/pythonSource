# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결  : 현재는 테이블이 있기때문에 연결의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# 커서 획득
cursor = conn.cursor()

# sql = "update users set username = ? where id = ?"
# cursor.execute(sql, ("kang", 3))

sql = "update users set username = :username where id = :id"
cursor.execute(sql, {"username": "hong", "id": 3})


for user in cursor.execute("select * from users").fetchall():
    print(user)

conn.close()