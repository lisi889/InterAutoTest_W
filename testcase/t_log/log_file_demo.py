import logging

#输出到控制台
#1设置loggin名称
logger = logging.getLogger("log_file_demo")
#2设置log级别
logger.setLevel(logging.DEBUG)
#3创建handler
fh_stream = logging.StreamHandler()
#然后再写入文件
fh_file = logging.FileHandler("./test.log")

#4设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)
#5定义输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
#6添加handle
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
#7运行输出

logger.info("this is info ")
logger.debug("this is debug")
logger.warning("this is warning")