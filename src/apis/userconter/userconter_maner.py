#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-06 10:56
# @Author : apple
# @Software: PyCharm
import codecs
import json
import requests
import logging

# 被继承的类作为参数传过去
from src.apis.baseapis_ke import BaseAPI_KE
from src.initialization.sysconfig import sys_cfg


class Zxz_User_Maner(BaseAPI_KE):
    # 初始化当前类
    def __init__(self):
        # 初始化被调用类，并且self作为参数传入
        BaseAPI_KE.__init__(self)
        logging.info('init member api')
        #
        self.shoucang_url= sys_cfg.get ( "apiurl", "shoucang" )

        # # 获取读取人员的URL
        # self.read_member_url=sys_cfg.get('contact_para','get_member_url')
        # self.paramall = {'access_token': self.get_token ( self.secure )}
    #创建新建人员
    def creat_member(self,filename):
        # 读取测试文件（json）并设置编码为utf-8
        with codecs.open(filename,'r',encoding='utf8') as f:
            # 文件转为json并设置编码
            json_object = json.loads(f.read(),encoding = 'utf8')
            # 设置URL的参数
            param ={'access_token':self.get_token(self.secure)}
            # 调用requests的封装方法
            self.post_json(self.creat_member_url,json_object,param)
            # logging.info('返回结果：',str(self.post_json(self.creat_member_ur,json_object,param)))
    #读取人员id---方法1
    def reaod_member(self):
        # with codecs.open(filename,'r',encoding='utf8') as f222:
            paramid={'access_token': self.get_token ( self.secure ),'userid':'ZhangXiaoZhe'}
            # json_object = json.loads(f222.read(),encoding='utf8')
            # self.post_json(self,json_object,paramid)
            # requests.get(self.read_member_url,paramid)
            # logging.info('返回结果：+++++++++++++',str(requests.get(self.read_member_url,paramid)))
            return requests.get(self.read_member_url,paramid)

    # 读取成员列表id---方法2
    def get_member_list(self, userid):
        param = {"access_token": self.get_token ( self.secure ), "userid": userid}
        print('ttttt'+userid)
        print(str(requests.get(self.read_member_url,params=param)))
        return requests.get ( self.read_member_url, params=param )
    # 收藏功能
    def rept_user(self):
        print("00000"+str(self.get_token()))
        headers = {
            'Authorization': self.get_token(),
            'Content-Type': 'application/json'
        }
        dd= {"courseId":"38","isCollection":1}
        resee=requests.post("https://yuyouyou.bjjh.org.cn/yx/course/courseCollection/collection",json=dd,headers=headers).json()
        print(resee)
        return resee

        # 收藏功能2
    def rept_user2(self):
            dd = {"courseId": "38", "isCollection": 1}
            print(self.shoucang_url+"999999999")
            logging.info(self.shoucang_url+"我爱你")
            self.post_json2(dd,self.shoucang_url)



    #读取多个文件 创建用户，对应member1和member2
    def creat_memner_more(self, file_name):
        new_member = self.get_new_member( file_name )
        param = {"access_token": self.get_token ( self.secure )}

        logging.debug ( "url=" + str ( self.creat_member_url ) )
        logging.debug ( "param=" + str ( param ) )

        self.post_json ( self.creat_member_url, json_obj=new_member, params=param )

  # 读取json文件，文件中只有一个成员信息 ，对应member1.json格式
    def get_new_member(self,file_name):
        with codecs.open(file_name,'r',encoding='utf8') as f:
            json_object = json.loads(f.read(),encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object
    #     返回的case的json对象
    def get_json_objcet(self,filename,caseid):
        with codecs.open(filename,'r',encoding='utf8') as f:
            jsonfileobj= json.loads(f.read(),encoding='utf8')
            jsonobjcase=jsonfileobj.get(caseid)
            logging.debug(jsonfileobj+str(jsonobjcase))
            return jsonobjcase
    # 创建人员的时候，一个json文件有多个用例
    def creat_memner_bymorejson(self,json_obj):
        param ={'access_token':self.get_token(self.secure)}
        self.post_json(self.creat_member_url,json_obj,param=param)
        #     返回的case的json对象

    def get_json_objcet_zong(self, filename, casename,casetype):
        with codecs.open ( filename, 'r', encoding='utf8' ) as f:
            jsonfileobj = json.loads ( f.read (), encoding='utf8' )
            print(filename+casename)
            case_json_object = jsonfileobj.get(casename).get( casetype)
            logging.debug ( 'json字典返回结果为' + str ( case_json_object ) )
            return case_json_object

 # 创建人员的时候，一个json文件有多个用例
    def creat_memner_re_zong(self,json_obj):
        param ={'access_token':self.get_token(self.secure)}
        self.post_json(self.creat_member_url,json_obj,param=param)

    # 动态更新参数，对应member4.json格式,封装读取json文件返回为字典
    def get_json_obj_from_file_with_reqres(self, file_name, testcase_name, type):
            with codecs.open ( file_name, 'r', encoding='utf8' ) as f:
                multiple_json_object = json.loads ( f.read (), encoding='utf8' )
                case_json_object = multiple_json_object.get ( testcase_name ).get ( type )
                logging.debug ( 'json_object' + str ( case_json_object ) )
                return case_json_object


 # 创建成员 发送-- reaques的post请求
    def create_member_by_json_obj(self,json_object):
        param = {'access_token':self.get_token(self.secure)}
        logging.debug("params:" + str(param))
        self.post_json(self.creat_member_url,json_object,params=param)

 # 创建成员 发送-- reaques的post请求
    def create_member_by_json_obj2(self,json_object):
        # param = {'access_token':self.get_token(self.secure)}
        # logging.debug("params:" + str(param))
        # self.post_json(self.creat_member_url,json_object,params=param)
        dd = {"courseId": "38", "isCollection": 1}
        print(self.shoucang_url+"999999999")
        logging.info(self.shoucang_url+"我爱你")
        self.post_json2(json_object,self.shoucang_url)