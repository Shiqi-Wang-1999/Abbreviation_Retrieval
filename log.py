import configparser
import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
"""
设置日志
"""


class Logger(object):
    def __init__(self):
        self.logger_level = logging.INFO
        self.logger_format = '%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] %(message)s'
        self.logger_filepath = os.path.join(BASE_DIR, 'log.log')
        self.logger_out = True
        # print(self.logger_filepath)
        logger = logging.getLogger('test')
        logger.setLevel(self.logger_level)
        format_logger = logging.Formatter(self.logger_format)
        if not logger.handlers:
            # 设置日志输出到文件（指定间隔时间自动生成文件的处理器  --按日生成）
            # filename：日志文件名，interval：时间间隔，when：间隔的时间单位， backupCount：备份文件个数，若超过这个数就会自动删除
            fileHandler = handlers.TimedRotatingFileHandler(filename=self.logger_filepath, when="D", backupCount=1,
                                                            encoding="utf-8")
            # 设置日志文件中的输出格式
            fileHandler.setFormatter(format_logger)
            # 将输出对象添加到logger中
            logger.addHandler(fileHandler)
            if (self.logger_out):
                streamHandler = logging.StreamHandler()  # 指定输出到console控制台
                streamHandler.setFormatter(format_logger)
                logger.addHandler(streamHandler)

        self.logger = logger


if __name__ == '__main__':
    log = Logger().logger
    log2 = Logger().logger
    log.info("dddd")
    log.warning("xxxx")
    log.error("xxxx")
    log.warning("xxxx")
    log.warning("xxxx")
    rootPath = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    print(rootPath)
    print(BASE_DIR)
