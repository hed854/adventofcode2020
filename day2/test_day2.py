import pytest
from day2 import SledPassword, TobogganPassword

# Passwords from the Sled Company
def test_sled_parse():
    data = "1-3 a: abcde"
    s = SledPassword(data)
    assert 1 == s.lower_bound
    assert 3 == s.upper_bound
    assert "a" == s.letter
    assert "abcde" == s.password

def test_sled_validate():
    a = SledPassword("1-3 a: abcde")
    assert True == a.validate()
    b = SledPassword("1-3 b: cdefg")
    assert False == b.validate()

def test_toboggan_parse():
    data = "1-3 a: abcde"
    t = TobogganPassword(data)
    assert ["1","3"] == t.position
    assert "a" == t.letter
    assert "abcde" == t.password

def test_toboggan_validate():
    a = TobogganPassword("1-3 a: abcde")
    assert True == a.validate()
    b = TobogganPassword("1-3 b: cdefg")
    assert False == b.validate()
    c = TobogganPassword("2-9 c: ccccccccc")
    assert False == c.validate()
