import pytest
from function.functions import func_1, func_2

def test_1():
    assert func_1(3) == 9
def test_2():
    assert func_2('Example of text') == 'EXAMPLE OF TEXT'



if __name__ == '__main__':
    pytest.main()

