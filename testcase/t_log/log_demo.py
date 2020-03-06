import logging

#设置配置信息
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#定义日志名称
logger = logging.getLogger("log_demo")

#打印信息info  debug
logger.info("info")
logger.debug("debug")
logger.warning("warning")