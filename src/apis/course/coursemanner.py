#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-09-04 15:10
# @Author : apple
# @Software: PyCharm
import codecs
import json
import logging

from src.apis.baseapis_ke import BaseAPI_KE
from src.initialization.sysconfig import sys_cfg


class CourseManner(BaseAPI_KE):
    def __init__(self):
        BaseAPI_KE.__init__(self)
        logging.info("init Course Api Test")
        self.gradesb=sys_cfg.get("apiurl","GradeSubject")
    # 查询首页-年级科目导航
    def getgradesubject(self,json_object):
        self.post_from_json(self.gradesb,json_object)
        # 动态更新参数，对应member4.json格式,封装读取json文件返回为字典

    def get_json_obj_from_file_with_reqres(self, file_name, testcase_name, type):
        with codecs.open ( file_name, 'r', encoding='utf8' ) as f:
            multiple_json_object = json.loads ( f.read (), encoding='utf8' )
            case_json_object = multiple_json_object.get ( testcase_name ).get ( type )
            logging.debug ( 'json_object' + str ( case_json_object ) )
            return case_json_object



