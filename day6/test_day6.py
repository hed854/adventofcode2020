import pytest
from day6 import parse_group, sum_group, parse_unanimous

def test_parse_group():
    t = parse_group("test_input", separator="")
    ref = [{"a","b","c"}, {"a","b","c"}, {"a","b","c"}, {"a"}, {"b"}]
    assert ref == t

def test_sum_group():
    t = parse_group("test_input", separator="")
    assert 11 == sum_group(t)
    t = parse_unanimous("test_input", separator="")
    assert 6 == sum_group(t)

def test_parse_unanimous():
    t = parse_unanimous("test_input", separator="")
    ref = [{"a", "b", "c"}, None, {"a"}, {"a"}, {"b"}]
    assert ref == t
