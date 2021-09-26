import logging
from config.address_config import *

"""basicconfig 局限性：
    1、中文的乱码问题
    2、不能同时往文件和屏幕上输出"""
"""logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')"""
class Logger():

    def __init__(self):
        self.logname = log_file
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")