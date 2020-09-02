#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-06 10:54
# @Author : apple
# @Software: PyCharm
import logging

from src.apis.userconter.userconter_maner import Zxz_User_Maner


class TestCreat_memberzxz:

    #  创建人员
    def testcreatRemeber (self):
        # 调用别的类时候，别的类有带括号（）有实例，也要都带过去
        User_maner = Zxz_User_Maner()
        assert  User_maner.rept_user().get("msg") =='请求成功'
        # User_maner.rept_user2()
        # res =User_maner.get_response()
        # # logging.info(res)
        # assert res.get('msg') == '请求成功'




