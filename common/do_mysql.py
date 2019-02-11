# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 20:51
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : do_mysql.py
import  mysql.connector
from conf import project_path
from common.my_log import MyLog
from common.read_config import ReadConfig

logger=MyLog()
class DoMysql:
    def do_mysql(self,sql):
        config=eval(ReadConfig().read_config(project_path.db_conf_path,'DATABASE','config'))
        cnn=mysql.connector.connect(**config)
        cursor=cnn.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchone()
            return result
        except Exception as e:
            logger.error('查询数据出错了，报错是:%s'%e)
        finally:
            cursor.close()
            cnn.close()

if __name__ == '__main__':
     sql='select leaveamount from member where mobilephone=13448773598'
     result=DoMysql().do_mysql(sql)
     print(int(result[0]))
