import logging

import os

from config import Conf
import datetime
from config.Conf import ConfigYaml

#定义日志级别的映射
log_l = {
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR

}

#定义类
class Logger:
#定义参数
    #输出文件名称  loggername  日志级别
    def __init__(self,log_file,log_name,log_level):
        self.log_file = log_file  #配置文件  扩展名
        self.log_name = log_name
        self.log_level = log_level  #配置文件

#输出控制台
        #1设置loggin名称
        self.logger = logging.getLogger(self.log_name)
        #2设置log级别
        self.logger.setLevel(log_l[self.log_level])
        #3创建handler 输出到控制台
        #先判断handle是否存在
        if not self.logger.handlers:

            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
            fh_stream.setFormatter(formatter)

            #然后再写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            #6添加handle
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)

#初始化参数数据
#日志文件名称  日志文件级别
#日志文件名称  logs目录+ 当前时间 +扩展名
log_path = Conf.get_log_path()

#当前时间
current = datetime.datetime.now().strftime("%Y-%m-%d")

#扩展名
log_extension = ConfigYaml().get_cont_log_extension()
logfile = os.path.join(log_path,current+log_extension)
# print("----------",logfile)

#日志级别
loglevel = ConfigYaml().get_cont_log()
# print(loglevel)

#对外方法，初始log工具，提供其他类使用
def my_log(log_name = __file__):
    return Logger(log_file = logfile,log_name =log_name,log_level=loglevel).logger

if __name__ == "__main__":
    my_log().debug("this is debug")