#! /usr/bin/env python3
import pytest

@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (2, 3, 5), (3, 5, 8)])
def test_sum(num1, num2, expected):
    assert num1 + num2  == expected

def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        1/0

def strip(s: str) -> str:
    return s.strip()

def test_strip_both_sides():
    print('test_strip_both_sides')
    # test both sides
    assert strip('  hello  ') == 'hello'

def test_strip_left_side():
    #  test left side
    assert strip('  hello') == 'hello'

def test_strip_right_side():
    # test right side
    assert strip('hello  ') == 'hello'

def test_strip_no_spaces():
    # test no spaces
    assert strip('hello') == 'hello'