__author__ = 'zz'
import unittest
import time
import HTMLTestRunnerNew
from common.send_email import sendEmail
from conf import project_path
from common.test_http_request_old import TestHttpRequest


suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取当前时间
file_path=project_path.report_path+'\\test'+now+'.html'


#执行用例
with open(file_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester='summer')
    runner.run(suite)

#发送邮件
sendEmail().send_email('204893985@qq.com',file_path)