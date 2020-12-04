#!/usr/bin/env python
"""
Advent of Code 2020 Day 4: Passport Processing
https://adventofcode.com/2020/day/4
"""

class Passport():
    def __init__(self, data):
        self.data = data
        self.fields = self.parse()

    def parse(self):
        parsed_dict = {}
        for i in self.data.split():
            pair = i.split(":")
            parsed_dict[pair[0]] = pair[1]
        return parsed_dict

    def validate(self):
        if len(self.fields) == 8:
            return True
        elif 'cid' not in self.fields and len(self.fields) == 7:
            return True
        else:
            return False


def batch_import(input_file):
    batch = []
    with open(input_file) as f:
        a = []
        for line in f:
            if len(line.strip()) != 0:
                # Accumulate lines
                a.append(line.strip())
            else:
                # Empty lines are the separator
                # Merge accumulated lines
                batch.append(" ".join(a))
                # Empty the list
                a = []
        # Last item is processed manually lol
        batch.append(" ".join(a))
        return batch

passports_validation = [Passport(i).validate() for i in batch_import("input")]
print(passports_validation.count(True))
