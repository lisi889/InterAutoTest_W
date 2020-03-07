import pymysql
from utils.LogUtil import my_log
#创建封装类
class Mysql:
#初始化
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        self.currsor = self.conn.cursor(cursor=pymysql.cursors.DictCursor) #返回变成字典形式
#创建查询、执行方法
#单个查询
    def fetchone(self,sql):
        self.currsor.execute(sql)
        return self.currsor.fetchone()
#多个查询
    def fetchall(self,sql):
        self.currsor.execute(sql)
        return self.currsor.fetchall()

#执行
    def exec(self,sql):
        try:
            if self.conn and self.currsor:
                self.currsor.execute(sql)
                self.conn.commit()  #---这里开始写错了
        except Exception as e:
            self.conn.rollback()
            my_log().error("mysql执行失败")
            my_log().error(e)
            return False
        return True
#关闭对象
    def __del__(self):
        if self.currsor is not None:
            self.currsor.close()
        if self.conn is not None:
            self.conn.close()
if __name__ == "__main__":
    mysql = Mysql("127.0.0.1",
                  "root",
                  "mysql",
                  "test_27",
                  charset="utf8",
                  port=3306)
    # res = mysql.fetchone("select * from roles")
    # print(res)
    res = mysql.exec("update roles set name='大大' where id=1")  #---这里开始用错了方法用成了fetchone
    print(res)
#连接databases
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="mysql",
#     database="test_27",
#     charset="utf8",
#     port=3306
# )
#获取执行sql的光标对象
# currsor = conn.cursor()

#执行sql
# sql = "select * from roles"
# currsor.execute(sql)
# res = currsor.fetchone()
# print(res)
#关闭对象
# currsor.close()
# conn.close()