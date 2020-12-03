import pytest
from day1 import slice_list, sum_list

def test_sum():
    data = [1, 2, 3, 4]
    assert 10 == sum_list(data)

def test_slice_list():
    data = [1, 2, 3, 4]
    assert [2, 3, 4] == slice_list(data, 0)
    assert [4] == slice_list(data, 2)



