import pytest
"""
创建类和测试方法
创建数据
创建参数化
运行
"""
class TestOne:
    #创建测试数据
    data_list = [("xiaoming","123456"),("xiaohong","456789")]

    @pytest.mark.parametrize(("name","password"),data_list)
    def test_a(self,name,password):
        print("test_a")
        print(name,password)
        assert 1

if __name__ == "__main__":
    pytest.main(["pytest_two.py"])