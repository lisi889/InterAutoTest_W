import re
import subprocess

from config.Conf import ConfigYaml
from utils.EmailUtil import SendEmail
from utils.MysqlUtil import Mysql
import json
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
p_data = re.compile('\${(.*)}\$')
log = my_log()

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

def json_parse(data):
    """格式化字符，转换json"""
    # 判断header是否存在，json转义
    # if headers:
    #     header = json.loads(headers)
    # else:
    #     header = headers

    json.loads(data) if data else data
# 查询方法、公共方法
def res_find(data,patten_data=p_data):
    # patten = re.compile('\${(.*)}\$')
    patten = re.compile(patten_data)
    re_res = patten.findall(data)
    return re_res
#替换
def res_sub(data,replace,patten_data=p_data):
    patten = re.compile(patten_data)
    re_res = patten.findall(data)
    if re_res:
        return  re.sub(patten_data,replace,data)
    return re_res

def assert_db(db_name,result,db_verify):
    assert_util = AssertUtil()
    # sql = init_db("db_1")
    sql = init_db("db_name")
    # 查询sql，excel定义好的
    db_res = sql.fechone(db_verify)
    log.debug("数据库查询结果：{}".format(str(db_res)))
    # 数据库的结果与接口返回的结果验证
    # 获取数据库的结果key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库的结果，接口的结果
    for line in verify_list:
        # res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
    # 验证
    assert_util.assert_body(res_line, res_db_line)

#验证请求中是否${},返回${}￥内容也作为公共方法
def params_find(headers,cookies):
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies

def allure_report(report_path,report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """

    #执行命令 allure generate
    allure_com = "allure generate --clean %s -o %s" % (report_path,report_html)
    # subprocess.call
    log.info("报告地址")
    try:
        subprocess.call(allure_com,shell=True)
    except Exception as e:
        print(e)
        log.error("执行用例失败，请检查一下测试环境相关配置")
        raise
def send_mail(report_html_path="",content= "",title="测试"):
    """发送邮件"""
    # from config.Conf import ConfigYaml
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()


if __name__ =="__main__":
    pass
    # init_db("db_1")
    # print(res_find('{"Aythorization":"JWT ${token}$"}'))
    # print(res_sub('{"Aythorization":"JWT ${token}$"}',"123"))
