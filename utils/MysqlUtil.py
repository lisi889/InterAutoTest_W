import pymysql
#连接databases
conn = pymysql.connect(
    host= ,
    user=,
    password= ,
    databases= ,
    charset= ,
    port= ,
)
#获取执行sql的光标对象
currsor = conn.cursor()

#执行sql
sql = "select username,password from tb_users"
currsor.execute(sql)
res = currsor.fetchone()
print(res)
#关闭对象
currsor.close()
conn.close()