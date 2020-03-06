import pytest
"""
创建类和测试方法
创建数据
创建参数化
运行
"""
class TestOne:
    #创建测试数据
    data_list = ["xiaoming","xiaohong"]

    @pytest.mark.parametrize("name",data_list)
    def test_a(self,name):
        print("test_a")
        print(name)
        assert 1

if __name__ == "__main__":
    pytest.main(["pytest_one.py"])