__author__ = 'zz'

import requests#完成HTTP请求
class HttpRequest:#HttpRequest(url,param).http_request(method,cookies)
    def __init__(self,url,param):
        self.url=url
        self.param=param

    def http_request(self,method,cookies=None):#定义了默认值
        if method.upper()=='GET':
            res=requests.get(self.url,self.param,cookies=cookies)
        elif method.upper()=='POST':
            res=requests.post(self.url,self.param,cookies=cookies)
        else:
            print("你的请求方式不对！")
        return res


if __name__ == '__main__':
    register='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    login='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    recharge='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    register_param={'mobilephone': '13148773463', 'pwd' : '123456'}
    login_param={'mobilephone': '13148773463', 'pwd' : '123456'}
    recharge_param={'mobilephone': '13148773463', 'amount' : '1000'}
    #注册
    res_register=HttpRequest(register,register_param).http_request('get')
    print(res_register.json())

    #登录  cookie 是必须登录了之后才会生成的？
    res_login=HttpRequest(login,login_param).http_request('get')
    print(res_login.json())
    cookies=res_login.cookies#登录请求发出去之后才能获取cookie
    print(cookies)

    #充值
    res_recharge=HttpRequest(recharge,recharge_param).http_request('get',cookies)
    print(res_recharge.json())
    print(res_recharge.cookies)