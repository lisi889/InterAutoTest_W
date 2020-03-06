import pytest
#
def test_1():
    a = True
    assert a


def test_2():
    a = True
    assert not a


def test_3():
    a = "hello"
    b = "hello word"
    assert a in b


def test_4():
    a =b = "hello"
    assert a == b

def test_5():
    a = "hello "
    b = "hello word"
    assert a != b

if __name__ == "__main__":
    pytest.main(["pytest_assert.py"])