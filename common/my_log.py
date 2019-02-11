__author__ = 'zz'
import logging
from conf import project_path
class MyLog:
    def my_log(self,msg,msg_level,log_name='auto_cases',level='DEBUG',file_path=project_path.log_path):
        logger=logging.getLogger(log_name)
        logger.setLevel(level)#日志收集器的级别

        #输出渠道 相对路径
        fh=logging.FileHandler(file_path,encoding='UTF-8')
        sh=logging.StreamHandler()

        fh.setLevel(level)#输出渠道的级别
        sh.setLevel(level)

        formatter=logging.Formatter('[%(levelname)s]%(asctime)s[日志信息]:%(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        #对接日志收集器 以及输出渠道
        logger.addHandler(sh)
        logger.addHandler(fh)
        if msg_level=='DEBUG':
            logger.debug(msg)
        elif msg_level=='INFO':
            logger.info(msg)
        elif msg_level=='WARNING':
            logger.warning(msg)
        elif msg_level=='ERROR':
            logger.error(msg)
        elif msg_level=='CRITICAL':
            logger.critical(msg)
        #使用完成后要记得移除handler
        logger.removeHandler(fh)
        logger.removeHandler(sh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


if __name__ == '__main__':
    MyLog().info('silly')
    #关于这个  懂得同学 就自己去写 不懂的就算了  直接用老师
    #知道怎么用老师的这个my_log
