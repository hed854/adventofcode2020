#!/usr/bin/env/python
"""
advent of code 2020 day 5: binary boarding
https://adventofcode.com/2020/day/5
"""

# Represent the plane as 2 lists
# The FRONT of the plane is on the left side
plane_data = {
    "rows": [i for i in range(128)],
    "cols": [i for i in range(8)]
}

def seat_id(row, col):
    return row * 8 + col


def auto_bisect(data, order):
    """
    Split the input list in two
    and returns the wanted half
    """
    # use int division
    half = len(data)//2
    if order == "F" or order =="L":
        return data[:half]
    elif order =="B" or order == "R":
        return data[half:]
    else:
        # idk
        pass


def traverse(data, orders):
    step = 0
    while len(data) > 1:
        data = auto_bisect(data, orders[step])
        step = step + 1
    return(data[0])


def resolve_seat(boarding_pass):
    row = traverse(plane_data["rows"], boarding_pass[:7])
    col = traverse(plane_data["cols"], boarding_pass[-3:])
    return seat_id(row, col)


def find_empty_seat(seats):
    i = 0
    while i <= len(seats):
        a = seats[i:i+2]
        # seats are reverse sorted
        if len(a) == 2 and a[0] - a[1] != 1:
            return(a)
        else:
            pass
        i = i + 1


with open("input") as f:
    seats = []
    err = 0
    for boarding_pass in f:
        if len(boarding_pass.rstrip()) != 0:
            seats.append(resolve_seat(boarding_pass.rstrip()))
    seats.sort(reverse = True)
    print(f"Here's an empty seat: {find_empty_seat(seats)}")
