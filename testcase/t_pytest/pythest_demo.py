import pytest


#普通方法
def func(x):
    return x+1

#断言的方法
def test_a():
    print("----test_a----")
    assert func(3) == 5
@pytest.mark.flaky(reruns = 3,reruns_delay = 2)
def test_b():
    print("----test_b----")
    assert 1

#运行pytest
"""
使用代码执行
"""
if __name__ =="__main__":
    pytest.main(["-s","pythest_demo.py"])