#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-09-01 13:03
# @Author : apple
# @Software: PyCharm
import configparser
# def readconif(cnf_file):
#     conf=configparser.ConfigParser()
#     conf.read(cnf_file,encoding="utf-8")
#     # 必须有返回值，如果没有的话在调用的地方没有相应的方法
#     return conf
# cong_obj=readconif('../../cfg/auto.cfg')

def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file,encoding="utf-8")
    return cfg

# 读取cfg文件,并获取对象
sys_cfg = read_config("/Users/apple/PycharmProjects/yuyouyou/cfg/auto.cfg")
if __name__ == '__main__':
    print(sys_cfg.get('urlhost','urlOriginTest'))



