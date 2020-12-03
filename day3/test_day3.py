import pytest
from day3 import Map

def test_map_coordinates():
    t = Map("test_input")
    # non wrapped
    assert "." == t.get_tile(0,0)
    assert "#" == t.get_tile(3,0)
    assert "." == t.get_tile(0,3)
    assert "." == t.get_tile(3,3)
    # wrapped coordinates
    assert "." == t.get_tile(12,0)
    assert "." == t.get_tile(14,0)
    assert "." == t.get_tile(12,0)
    assert "." == t.get_tile(12,0)
