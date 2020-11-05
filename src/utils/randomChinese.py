#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-06 07:52
# @Author : apple
# @Software: PyCharm
import random
import pytest
# 生成随机中文字符

def get_random_char(number):
    val_list =[]
    for nu in range(0,number):
        val_list.append(chr(random.randint(0x4e00,0x9fbf)))
    return ''.join(val_list)
    print(val_list)