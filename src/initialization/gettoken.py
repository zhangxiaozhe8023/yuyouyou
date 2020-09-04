import logging
import requests
# 静态方法获取token只运行一次
from src.initialization.sysconfig import sys_cfg


class GetAccessToken:
    logging.basicConfig ( level=logging.DEBUG )
    _token = ""
    @classmethod
    def get_token(cls):
            if len ( cls._token ) == 0:
                cls._token = cls.get_token_new ()
            return cls._token
    @classmethod
    def get_token_new(cls):
        pames = {"username": "zxz002", "password": "123456"}
        # 使用requests的get请求获取response对象
        token_res = requests.post ( sys_cfg.get("urlhost","urlOriginTest") + sys_cfg.get("apiurl","loginurl"), json=pames )
        # 把response对象 转为json串
        token_res_json = token_res.json()
        logging.info('登录的response' + str(token_res_json))
        # 获取accesstoken的值
        access_token = token_res_json.get('data').get('token')
        print("看看运行几次")
        return access_token
