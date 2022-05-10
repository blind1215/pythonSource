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

# sql = """
#     select * from users
# """
# cursor.execute(sql)

sql = """
    select * from users where id = %s
"""
cursor.execute(sql % 4)

print(cursor.fetchone())

cursor1 = conn.cursor(pymysql.cursors.DictCursor)
cursor1.execute("select * from users where id In(%s,%s)" % (3, 5))

for row in cursor1.fetchall():
    print(row["username"])


conn.commit()
conn.close()
