# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결  : 현재는 테이블이 있기때문에 연결의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# 커서 획득
cursor = conn.cursor()

# sql = "delete from users where id = ?"
# cursor.execute(sql, (3,))

# sql = "delete from users where id = :id"
# cursor.execute(sql, {"id": 4})

print("users db delete : ", cursor.execute("delete from users").rowcount)

for user in cursor.execute("select * from users").fetchall():
    print(user)

conn.commit()
conn.close()