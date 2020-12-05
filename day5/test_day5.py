import pytest
from day5 import seat_id, auto_bisect, traverse, resolve_seat, find_empty_seat

def test_seat_id():
    assert 567 == seat_id(70, 7)
    assert 119 == seat_id(14, 7)
    assert 820 == seat_id(102, 4)

def test_auto_bisect():
    data = [1, 2, 3, 4, 5, 6]
    assert [1, 2, 3] == auto_bisect(data, "F")
    assert [4, 5, 6] == auto_bisect(data, "B")

def test_traverse():
    # plane rows
    data = [i for i in range(128)]
    partial_orders = "FBFBBFF"
    assert 44 == traverse(data, partial_orders)
    partial_orders = "BFFFBBF"
    assert 70 == traverse(data, partial_orders)
    partial_orders = "FFFBBBF"
    assert 14 == traverse(data, partial_orders)

    # plane cols
    data = [i for i in range(8)]
    partial_orders = "RLR"
    assert 5 == traverse(data, partial_orders)
    partial_orders = "RRR"
    assert 7 == traverse(data, partial_orders)

def test_resolve_seat():
    boarding_pass = "FBFBBFFRLR"
    assert 357 == resolve_seat(boarding_pass)
    boarding_pass = "BFFFBBFRRR"
    assert 567 == resolve_seat(boarding_pass)
    boarding_pass = "FFFBBBFRRR"
    assert 119 == resolve_seat(boarding_pass)
    boarding_pass = "BBFFBBFRLL"
    assert 820 == resolve_seat(boarding_pass)

def test_find_empty_seat():
    seats = [7,6,5,3,2]
    assert [5,3] == find_empty_seat(seats)
