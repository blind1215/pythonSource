# SQLite : 내장 데이터베이스 (응용 프로그램에 넣어서 사용)
import sqlite3
from datetime import datetime

# sqlite 버전 확인
print("sqlite.version : {} ".format(sqlite3.version)) # sqlite.version : 2.6.0

# 날짜 / 시간 생성
now = datetime.now()
print(now) # 2021-03-09 11:05:15.863775

# 날짜를 원하는 대로
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowDateTime) # 2021-03-09 11:06:51