import os
import pytest

if __name__ == '__main__':
    # 第一个参数vs，详细日志
    # 文件夹的路径
    # 运行整个文件夹
    # pytest.main(['-vs', "case"])
    # 运行单个用例文件
    pytest.main(["-vs", "case/test_likeshop_01.py"])
    # 多个用例文件
    # pytest.main(["-vs","case/test_baotao_02.py","case/test_baotao_01.py"])
    # 运行单个用例函数
    # pytest.main(["-vs", "case/test_baotao_02.py::TestBaotao02::test_02"])
    os.system('allure generate ./json -o ./report --clean')
