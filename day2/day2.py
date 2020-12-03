#!/usr/bin/env python
"""
Advent of Code 2020 Day 2: Password Philosophy
https://adventofcode.com/2020/day/2
"""

class SledPassword():
    """
    Password parsing & policies from the Sled Company!!
    """
    def __init__(self, data):
        self.data = data
        self.lower_bound, self.upper_bound, self.letter, self.password = self.parse()

    def parse(self):
        # Split by space first
        parsed = self.data.split()
        bounds = parsed[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        letter = parsed[1][0]
        password = parsed[2]
        return lower_bound, upper_bound, letter, password

    def validate(self):
        count = 0
        for i in self.password:
            if i == self.letter:
                count = count + 1
        if count >= self.lower_bound and count <= self.upper_bound:
            return True
        else:
            return False

class TobogganPassword():
    """
    Password parsing & policies from the Toboggan Company!!
    """
    def __init__(self, data):
        self.data = data
        self.position, self.letter, self.password = self.parse()
    def parse(self):
        parsed = self.data.split()
        position = parsed[0].split('-')
        letter = parsed[1][0]
        password = parsed[2]
        return position, letter, password

    def validate(self):
        count = 0
        for i in self.position:
            if self.password[int(i)-1] == self.letter:
                count = count + 1
        if count == 1:
            return True
        else:
            return False

# First half (Sled passwords)
#with open("input") as f:
#    data = f.readlines()
#    validated_passwords = 0
#    for entry in data:
#        sp = SledPassword(entry)
#        if sp.validate():
#            validated_passwords = validated_passwords + 1
#    print(validated_passwords)

# Second half (Toboggan passwords)
with open("input") as f:
    data = f.readlines()
    validated_passwords = 0
    for entry in data:
        tp = TobogganPassword(entry)
        if tp.validate():
            validated_passwords = validated_passwords + 1
    print(validated_passwords)
