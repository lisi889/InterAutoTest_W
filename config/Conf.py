#获取项目目录
#1获取项目当前路径
import os
from utils.YamlUtil import YamlReader

current = os.path.abspath(__file__)
# print(current)

BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)

#2获取config路径
_config_path = BASE_DIR + os.sep + "config"
# print(_config_path)
#3获取conf。yaml路径
_config_file = _config_path + os.sep + "conf.yml"
print(_config_file)

#定义log文件路径
_log_patch = BASE_DIR + os.sep + "logs"

#定义db_conf路径
_db_config_file = _config_path + os.sep + "db_conf.yml"

#定义data目录
_data_config_path = BASE_DIR +os.sep + "data"

#定义report目录的路径
_report_path = BASE_DIR + os.sep +"report"

def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

def get_log_path():
    return _log_patch

def get_db_conf_get():
    return _db_config_file

def get_data_path():
    return _data_config_path

def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return _report_path

#读取配置文件
#创建类
class ConfigYaml:
#初始化ymal
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_conf_get()).data()
        # print("-----------" % self.config )

# 获取信息
    #定义方法获取需要的信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]
    #获取日志级别信息
    def get_cont_log(self):
        return self.config["BASE"]["log_level"]

    #获取文件扩展名
    def get_cont_log_extension(self):
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self,db_alias):
        return self.db_config[db_alias]

    def get_excel_file(self):
        """获取excel用例名称"""
        return self.config["BASE"]["test"]["case_file"]
    def get_excel_sheet(self):
        """获取sheet用例名称"""
        return self.config["BASE"]["test"]["case_sheet"]

    def get_email_info(self):
        """获取邮件配置信息"""
        return self.config["email"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_cont_log())
    # print(conf_read.get_cont_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    # print(conf_read.get_db_conf_info("db_2"))
    # print(conf_read.get_db_conf_info("db_3"))
    print(conf_read.get_excel_file())
    print(conf_read.get_excel_sheet())
    print(conf_read.get_email_info())