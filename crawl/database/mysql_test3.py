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

cursor.execute(sql, ("Park", "park@naver.com", "010-4568-1234", "park.com"))
conn.commit()
conn.close()
