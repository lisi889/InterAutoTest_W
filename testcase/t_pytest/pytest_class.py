import pytest
"""
定义类
创建测试方法test
创建setup_class teardown_class
运行查看结果
"""
class TestClass:
    #创建
    def setup_class(self):
        print("-----setup_class----")

    def teardown_class(self):
        print("-----teardown_class----")


    # 创建测试方法
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

if __name__ == "__main__":
    pytest.main(["-s","pytest_class.py"])