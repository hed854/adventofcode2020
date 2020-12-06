#!/usr/bin/env python
"""
advent of code 2020 day 6: custom customs
https://adventofcode.com/2020/day/6
"""

def parse_group(input_file, separator):
    """
    parse a file and groups together the entries, adding a custom separator
    a group ends either:
        - if it's the end of the file
        - if there's an empty line
    """
    with open(input_file) as f:
        groups = []
        temp = []
        for line in f:
            if len(line.strip()) != 0:
                # Accumulate lines
                temp.append(line.strip())
            else:
                # New group
                # Also uniq everything with a set
                groups.append(set(separator.join(temp)))
                temp = []
        # Last item is processed manually lol
        groups.append(set(separator.join(temp)))
        return groups

def parse_unanimous(input_file, separator):
    """
    parse a file and keeps only the unanimous answers
    in the group
    a group ends either:
        - if it's the end of the file
        - if there's an empty line
    """
    with open(input_file) as f:
        groups = []
        temp = []
        for line in f:
            if len(line.strip()) != 0:
                # Accumulate lines
                temp.append(line.strip())
            else:
                # Intersect everything
                unanimous = [set(i) for i in temp]
                res = unanimous[0].intersection(*unanimous) or None
                groups.append(res)
                temp = []
        # Last item is processed manually lol
        unanimous = [set(i) for i in temp]
        res = unanimous[0].intersection(*unanimous) or None
        groups.append(res)
        return groups


def sum_group(data):
    """
    Sum whatever is provided
    """
    sum = 0
    for i in data:
        if i is not None:
            sum = sum + len(i)
        else:
            # add nothing
            pass
    return sum

# Part 1
print(sum_group(parse_group("input", "")))

# Part 2
print(sum_group(parse_unanimous("input", "")))
