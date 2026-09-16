import pytest

from calculator import add, subtract, multiply, divide

def test_add(a, b):
    assert add(2, 3) == 5

def test_subtract(a, b):
  assert subtract(10, 4) == 6

def test_multiply(a, b):
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 4) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
