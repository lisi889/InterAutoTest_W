import pytest
"""
定义类
创建测试方法test
创建setup teardown
运行查看结果
"""

class TestFunc():
    #创建setup teardown
    def setup(self):
        print("-----setup----")
    def teardown(self):
        print("----teardown----")


    #创建测试方法
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")
#运行
if __name__=="__main__":
    pytest.main(["-s","pytest_func.py"])