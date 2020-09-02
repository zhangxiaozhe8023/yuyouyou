#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import requests

import pytest

from src.initialization.sysconfig import sys_cfg


class BaseAPI_KE:

    def __init__(self):
        logging.info('init base api interface')
        # 读取配置文件，通过导入包实现获取配置参数
        self.url_host = sys_cfg.get('urlhost','urlOriginTest')
        self.token_url = sys_cfg.get('apiurl', 'loginurl')
        # 定义空的resquen
        self.res =''
    # 公用的获取token,需要传入通讯录同步的secure
    def get_token(self):
        # 参数为企业ID和应用的凭证密钥
        pames={"username": "zxz002", "password": "123456"}
        # 使用requests的get请求获取response对象
        token_res=requests.post(self.url_host+self.token_url,json=pames)
        #把response字典 转为json串
        # print ("dddd"+ str(token_res.json ()) )
        token_res_json =token_res.json()

        logging.info ( 'BBBBBBBBBBB' + str(token_res_json))
        # 获取accesstoken的值
        re_acces_token=token_res_json.get('data').get('token')
        # print("666666"+str(re_acces_token))
        return re_acces_token
    # post请求的封装方法
    def post_json(self, url, json_obj, params=None,):
        # 如果有就传值，如果没有就不传params
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)
    def post_json2(self,dd,url):
        headers1 = {
            'Authorization': self.get_token (),
            'Content-Type': 'application/json'
        }
        logging.info ( "uuuuuurl" + self.url_host + url )
        self.res= requests.post(self.url_host+url,json=dd,headers=headers1)
        logging.info("返回值"+str(self.res.json()))


    # 封装get请求方法
    def get_json(self,url,parms):
        self.res_get=requests.get(url,parms)
    # 封装请求request-response的json返回结果
    def get_response(self):
        logging.debug('最后返回字符串'+str(self.res.json()))
        return self.res.json()
    def kdkdk(self):
        logging.debug("9999999999999")
    if __name__ == '__main__':
        pames={"username": "zxz002", "password": "123456"}
        relogin=requests.post("https://yuyouyou.bjjh.org.cn/yx/user/sso/login",json=pames)
        print(relogin.json())


