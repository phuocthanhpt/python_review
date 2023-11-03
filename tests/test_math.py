import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


@pytest.mark.math
def test_divide_by_0():
    with pytest.raises(Exception) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


'''
Test Multiplication with some scenarios:
1. Multiply with 0
2. Multiply with 1
3. Two positive integers
4. Positive with negative
5. Two negative 
6. Floats
'''

products = [
    (2, 0, 0),
    (5, 1, 5),
    (6, 7, 42),
    (8, -1, -8),
    (-7, -6, 42),
    (2.5, 3.5, 8.75),
]


@pytest.mark.parametrize('a,b,expected_result', products)
def test_multiplication_mark_parametrize(a, b, expected_result):
    assert a * b == expected_result
