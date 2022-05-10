# SQLite : 내장 데이터베이스(응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# database 생성 & 연결 
conn = sqlite3.connect("./crawl/database/test.db")

# Cursor 획득 : 디비에 일을 시킬라고 
cursor = conn.cursor()

# sql 실행 숫자지정없으면 기본값형태로 들어감 
sql = """ 
    Create table if not exists users(id integer primary key, username text,
    email text, website text, regdate text)
"""

cursor.execute(sql)
conn.commit()
conn.close()