__author__ = 'zz'
#专门完成http请求测试的  这是一个测试类
#DDT
import unittest

from ddt import ddt,data
from common.read_config import ReadConfig
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from common.my_log import MyLog
from conf import project_path
from common.do_mysql import DoMysql#进行数据库的操作
#用例的执行模式:
mode=ReadConfig().read_config(project_path.case_conf_path,'CASE','mode')
case_list=eval(ReadConfig().read_config(project_path.case_conf_path,'CASE','case_list'))

#数据以及ip地址
test_data=DoExcel(project_path.test_data_path,'test_data').read_data(mode,case_list)
IP=ReadConfig().read_config(project_path.http_conf_path,'HTTP','ip')

COOKIES=None#全局变量，初始值
MEMBER_ID=None#用户id 全局变量
LEAVE_AMONUT=None#余额 leave amount 全局变量

#日志类
logger=MyLog()

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel(project_path.test_data_path,'test_data')#操作Excel的实例
        #print("开始测试啦")
        logger.info("开始测试啦")

    @data(*test_data)
    def test_http_request(self,a):#a字典
        #print("测试数据是:",a)
        #print("目前正在执行第%s条用例"%a[0])
        logger.info("测试数据是:{0}".format(a))
        logger.info("目前正在执行第%s条用例"%a['case_id'])
        global COOKIES
        #判断params 是否需要做替换  根据你自己打的标记来做替换
        if a['params'].find('${member_id}')!=-1:
            param=a['params'].replace('${member_id}',str(MEMBER_ID))
            if param.find('${loan_id}')!=-1:
               loan_id=DoMysql().do_mysql('select id from loan where memberid='+str(MEMBER_ID))[0]
               param=param.replace('${loan_id}',str(loan_id))
        elif a['params'].find('${loan_id}')!=-1:
            loan_id=DoMysql().do_mysql('select id from loan where memberid='+str(MEMBER_ID))[0]
            param=a['params'].replace('${loan_id}',str(loan_id))
            global LEAVE_AMONUT
            LEAVE_AMONUT=DoMysql().do_mysql('select leaveamount from member where id='+str(MEMBER_ID))[0]
        else:
            param=a['params']

        res=HttpRequest(IP+a['url'],eval(param)).http_request(a['method'],cookies=COOKIES)
        #数据存储的方式 为什么要改成字典---方便取值  可以根据key去取value值
        if res.cookies!={}:#判断长度或者是判断是否为空{}
            COOKIES=res.cookies#只有登录才会产生cookies

        #检查数据库
        if a['check_sql']!=None:#是否需要对数据库进行检查？
            if a['check_sql'].find('${after_invest_money}')!=-1:
                query_sql=a['check_sql'].replace('${after_invest_money}',str(LEAVE_AMONUT-100))
            else:
                query_sql=a['check_sql']
            sql_result=DoMysql().do_mysql(eval(query_sql)['sql'])
            try:
                self.assertEqual(eval(query_sql)['expected'],str(sql_result[0]))
                check_sql_result='PASS'
            except AssertionError as e:
                check_sql_result='FAIL'
                raise e
            finally:
                self.t.write_data(int(a['case_id'])+1,2,str(sql_result),check_sql_result)

        if a['expect_result'].find('${member_id}')!=-1 and a['expect_result'].find('${regtime}')!=-1:
            #获取手机号 从params里面去获取手机号
            mobilephone=eval(a['params'])['mobilephone']
            #获取注册成功的用户id  此用例是根据注册--登录---充值一条流水做下来的
            member_id=DoMysql().do_mysql('select id from member where mobilephone='+mobilephone)[0]
            global  MEMBER_ID
            MEMBER_ID=member_id#这个是注册之后才会遇到的member_id
           #获取注册成功的用户的注册时间regtime
            regtime=DoMysql().do_mysql('select regtime from member where mobilephone='+mobilephone)[0]

           #这里要特别注意，我们自己在Excel里面做测试数据的时候 单引号和双引号要一致
            #因为后期结果比对 单引号和双引号 也需要做比对的！
            expected_result=eval(a['expect_result'])#先把期望值转成dict
            #替换id regtime 直接从字典去做替换
            expected_result['data']['id']=member_id
            expected_result['data']['regtime']=str(regtime)+'.0'
        else:
            expected_result=eval(a['expect_result'])

        try:
           self.assertEqual(expected_result,res.json())
           result='PASS'
        except AssertionError as e:
            result='Fail'
            raise e#跟return一样 中断代码
        finally:#
            self.t.write_data(int(a['case_id'])+1,1,str(res.json()),result)

    def tearDown(self):
        #print("结束测试了")
        logger.info("结束测试了")


