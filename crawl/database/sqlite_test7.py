# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결  : 현재는 테이블이 있기때문에 연결의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# 커서 획득
cursor = conn.cursor()

# sql = "select * from users where id =?"
# cursor.execute(sql, (3,))

# param = 4
# sql = "select * from users where id=%s"  # 문자열을 의미하는게 아니고 모든타입을 %s로 표시함
# cursor.execute(sql % param)

# param = {"id": 5}
# sql = "select * from users where id= :id"  # 딕션어리 형태
# cursor.execute(sql, param)

param = (3, 5)
sql = "select * from users where id in (?,?)"  # 딕션어리 형태
cursor.execute(sql, param)


# fecth : 실행된 결과를 가져오는것
# fetchone(),fetchmany(), fetchall()
print("first : ", cursor.fetchone())
print("All : ", cursor.fetchall())


conn.close()