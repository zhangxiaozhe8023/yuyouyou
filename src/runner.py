#! /usr/bin/env python
#coding=utf-8
import subprocess

import logging
import os
import sys

import pytest

#Add src root dirctory to PYTHONPATH by extend sys.path
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
# 读取全局配置文件

fileHandler = logging.FileHandler(filename="../log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    logging.info("Start to execute  automation cases")

    # pytest.main(['-s', '-q', '-v', '--alluredir', './result','./testcases'])
    #pytest.main(['-sq', 'testcases/'])
    # 执行创建部门测试用例
    # pytest.main(['-sq', 'testcases/contact/department/test_create_dept.py'])
    # 执行创建人员测试用例
    pytest.main ( ['-sq', 'testcases/user_zxz/test_read_zxz.py'] )
    # pytest.main ( ['-sq', 'testcases/user_zxz/test_read_zxz.py'] )

    #pytest.main(['-sq','--alluredir', '../log/testreport', 'testcases/contact/member/test_creat_main.py'])
    #print(subprocess.getstatusoutput('allure generate --clean ../log/testreport/ -o ../log/testreport/html'))
    logging.info("End to execute Intfacetiaon automaction cases")
