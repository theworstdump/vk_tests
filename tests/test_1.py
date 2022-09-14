import pytest
from function.functions import func_1, func_2, func_3

def test_1():
    assert func_1(3) == 9
def test_2():
    assert func_2('Example of text') == 'EXAMPLE OF TEXT'

@pytest.mark.parametrize("number, remain", [(-102, 0), (-101, 1), (-100, 2), (0, 0), (100, 1), (101, 2), (102, 0)])
def test_3(number, remain):
    assert func_3(number) == remain

if __name__ == '__main__':
    pytest.main()

