
import pytest
import allure

@allure.feature("接口测试，这是个一级标签")
class TestAllure:
    @allure.title("测试用例标题1")
    @allure.description("执行测试用例1的结果是test1")
    @allure.story("这是一个二级标签：test1")
    @allure.severity(allure.severity_level.BLOCKER)
    #测试方法
    def test_1(self):
        print("test1")

    @allure.title("测试用例标题2")
    @allure.description("执行测试用例1的结果是test2")
    @allure.story("这是一个二级标签：test1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test3")

    @allure.title("测试用例标题3")
    @allure.description("执行测试用例1的结果是test3")
    @allure.story("这是一个二级标签：test3")
    def test_3(self):
        print("test3")

    #动态方法-数据驱动
    @pytest.mark.parametrize("case",["case1","case2"])
    def test_4(self,case):
        print(case)
        allure.dynamic.title(case)  #动态获取


if __name__ == '__main__':
    pytest.main(["allure_demo.py"])