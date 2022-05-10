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

# delete
cursor = conn.cursor()


sql = """
    delete from users where id= %s
"""
cursor.execute(sql % 4)

cursor.execute("select * from users")

for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()
