from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
#定义init_db
def init_db(db_alias):
# db_1:
#   db_host: "127.0.0.1"
#   bd_user: "root"
#   db_password: "mysql"
#   bd_database: "test_27"
#   db_charset: "utf8"
#   db_port: "3306"
#初始化数据信息 通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["bd_user"]
    password = db_info["db_password"]
    database = db_info["bd_database"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"] ) #port需要转为int类型

#初始化mysql对象
    conn = Mysql(host,user,password,database,charset,port)
    print(conn)
    return conn

if __name__ =="__main__":
    init_db("db_1")