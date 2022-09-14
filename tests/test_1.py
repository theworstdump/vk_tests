import pytest
from function.functions import func_1, func_2, func_3, func_4

def test_1():
    assert func_1(3) == 9
def test_2():
    assert func_2('Example of text') == 'EXAMPLE OF TEXT'

@pytest.mark.parametrize("number, remain", [(-102, 0), (-101, 1), (-100, 2), (0, 0), (100, 1), (101, 2), (102, 0)])
def test_3(number, remain):
    assert func_3(number) == remain

@pytest.mark.parametrize("input_text, result", [('ABC', True), ('AbC', True), ('aBC', False), ('abc', False)])
def test_4(input_text, result):
    assert func_4(input_text) == result

if __name__ == '__main__':
    pytest.main()

