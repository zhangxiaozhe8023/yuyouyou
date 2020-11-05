#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-06 10:54
# @Author : apple
# @Software: PyCharm
import logging
import sys

import allure

from src.apis.userconter.userconter_maner import Zxz_User_Maner
from src.utils import comparator

@allure.feature("创建用户")

class Testdemo:

    #收藏接口
    def testshoucang (self):
        # 调用别的类时候，别的类有带括号（）有实例，也要都带过去
        User_maner = Zxz_User_Maner()
        # assert  User_maner.rept_user2().get("msg") =='请求成功'
        User_maner.rept_user2()
        res =User_maner.get_response()
        logging.info(res)
        assert res.get('msg') == '请求成功'

    @allure.story ( "创建用户test1" )
    def test_testcase3(self):
        # 如果类中只有一个方法，则可以用类名，获取类名
        class_name = self.__class__.__name__
        logging.info("classname====="+class_name)
        # 获取方法名、用例名  json数据中的参数必须设置为testcase1 与这里的方法名保持一致，才好获取
        case_name = sys._getframe ().f_code.co_name.split ( "_" )[1]
        logging.info('casename=='+case_name)
        user_managment = Zxz_User_Maner ()
        # 传递的参数为/testdata路径+类名.json，jsonobject名，jsonobject里的req类型object
        json_obj = user_managment.get_json_obj_from_file_with_reqres ( '../testdata/' + class_name + '.json',
                                                                  case_name, "req" )
        # 使用post请求参数为json串
        user_managment.uerpost_by_json_obj2 ( json_obj )
        # 获取请求后的返回值response
        live_create_res = user_managment.get_response ()
        # 传递的参数为/testdata路径+类名.json，jsonobject名，jsonobject里的res类型object
        std_json_obj_res = user_managment.get_json_obj_from_file_with_reqres ( '../testdata/' + class_name + '.json',
                                                                                 case_name,
                                                                                 "res" )
        # 获取JsonComparator对象
        json_comparator = comparator.JsonComparator ()
        # 断言两个json中的res中的值是否相等
        assert json_comparator.equal ( live_create_res, std_json_obj_res )
        # assert json_comparator.less_than(live_create_res, std_json_obj_res )

 #首页-年级科目导航1.1有更改
    def testGradeSubject (self):
        # 调用别的类时候，别的类有带括号（）有实例，也要都带过去
        User_maner = Zxz_User_Maner()
        # assert  User_maner.rept_user2().get("msg") =='请求成功'
        ddjson = {"phase": "1"}
        User_maner.postjson3(ddjson)
        res =User_maner.get_response()
        logging.info(res)
        assert res.get('msg') == '请求成功'