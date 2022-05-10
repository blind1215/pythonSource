import pymysql

# database 연결
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="biguser1",
    password="12345",
    db="bigdata",
    charset="utf8",
)

# print(conn)

# insert
cursor = conn.cursor()

sql = """
    insert into users(username,email,phone,website) values(%s,%s,%s,%s)
"""

userList = (
    ("Lee","lee@naver.com","010-3568-1234","lee.com"),
    ("Choi","choi@naver.com","010-8659-1234","choi.com"),
    ("Yoo","you@naver.com","010-4567-1234","yoo.com"),
)

cursor.executemany(sql, userList)
conn.commit()
conn.close()
