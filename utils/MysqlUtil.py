import pymysql
#连接databases
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="mysql",
    database="test_27",
    charset="utf8",
    port=3306
)
#获取执行sql的光标对象
currsor = conn.cursor()

#执行sql
sql = "select * from roles"
currsor.execute(sql)
res = currsor.fetchone()
print(res)
#关闭对象
currsor.close()
conn.close()