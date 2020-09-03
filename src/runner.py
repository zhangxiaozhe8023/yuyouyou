#! /usr/bin/env python
#coding=utf-8
import subprocess
import sys
import logging
import os
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

    # pytest.main(['-s', '-q', '-v', '--alluredir', 'result','testcases/'])
    #pytest.main(['-sq', 'testcases/'])
    # 执行创建部门测试用例
    # pytest.main(['-sq', 'testcases/contact/department/test_create_dept.py'])
    # 执行创建人员测试用例
    # pytest.main ( ['-sq', 'testcases/user_zxz/test_read2.py'] )
    pytest.main ( ['-sq', 'testcases/user_zxz/test_read_zxz.py'] )
    # 张晓哲自己写的创建人员测试用例
    # pytest.main(['-sq', 'testcases/contact/member/test_get_member_list.py'])
    # pytest.main(['-sq', 'testcases/contact/member/test_read_member_zxz.py'])
    # pytest.main(['-sq', 'testcases/contact/member_zxz/test_creat_member_zong.py'])
    # pytest.main(['-sq', 'testcases/contact/member_zxz/test_creat_main.py'])

    #pytest.main(['-sq', 'testcases/contact/department/test_update_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/department/test_delete_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/department/test_list_dept.py'])

    #pytest.main(['-sq','--alluredir', '../log/testreport', 'testcases/contact/member/test_creat_main.py'])
    #print(subprocess.getstatusoutput('allure generate --clean ../log/testreport/ -o ../log/testreport/html'))
    logging.info("End to execute Intfacetiaon automaction cases")
