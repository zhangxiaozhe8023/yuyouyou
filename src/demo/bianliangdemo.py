#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-09-04 10:24
# @Author : apple
# @Software: PyCharm
import logging

import requests

from src.utils.randomChinese import get_random_char

add = "http://c.biancheng.net/shell/"
def text():
    print("函数体内访问：",add)
text()
print('函数体外访问：',add)
if __name__ == '__main__':
    pames = {"username": "zxz002", "password": "123456"}
    headers1 = {
        'Content-Type': 'application/json'
    }
    # 使用requests的get请求获取response对象
    token_res = requests.post ( "https://zxkc.bjxjzd.com/api/yx/user/sso/login", json=pames,headers=headers1 )
    # 把response对象 转为json串
    # print ("dddd"+ str(token_res.json ()) )
    token_res_json = token_res.json ()
    logging.info ( '登录的response' + str ( token_res_json ) )
    # 获取accesstoken的值
    re_acces_token = token_res_json.get ( 'data' ).get ( 'token' )
    print(token_res.json())