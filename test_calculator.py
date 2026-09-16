import pytest

from calculator import add, subtract, multiply, divide

def test_add(a, b):
    assert add(2, 3) == 5

def test_subtract(a, b):
  assert subtract(10, 4)
