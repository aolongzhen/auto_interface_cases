# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 22:02
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test.py
str="{'status': 1, 'code': '10001', 'data': {'id': 15995, 'leaveamount': '1000.00', 'type': '1', 'pwd': 'E10ADC3949BA59ABBE56E057F20F883E', 'regtime': '2018-07-12 12:31:10.0', 'mobilephone': '13448773598', 'regname': '小蜜蜂'}, 'msg': '充值成功'}"

# import requests
# s=requests.session()
# dict_2={'memberId':'15995','title':'15995to_add_loan', 'amount' : '10000','loanRate':2,'loanTerm':'3','loanDateType':'0','repaymemtWay':'11','biddingDays':'5'}
# dict_1={'mobilephone':'13448773598','pwd':'123456'}
# s.post("http://119.23.241.154:8080/futureloan/mvc/api/member/login",dict_1)
# #s.post('http://119.23.241.154:8080/futureloan/mvc/api/loan/add',dict_2)
# #dict_3={'id' : '245', 'status' : '4'}
# #res=s.post('http://119.23.241.154:8080/futureloan/mvc/api/loan/audit',dict_3)
# dict_4={'memberId':'15995', 'password':'123456','loanId' : '245','amount' : '100'}
# res=s.post("http://119.23.241.154:8080/futureloan/mvc/api/member/bidLoan",dict_4)
# print(res.json())

str_2='testes'
print(str_2.replace('es','1'))

print(int(100))