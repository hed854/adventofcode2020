#!/usr/bin/env python
"""
Advent of Code 2020 Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3
"""

class Map():
    def __init__(self, input_file):
        with open(input_file) as f:
            self.partial_data = f.readlines()
        self.length = len(self.partial_data)
        self.width = len(self.partial_data[0])

    def expand(self):
        """
        Expand the basic map
        """
        pass

    def get_tile(self, x, y):
        # wrap the map width
        return self.partial_data[y][x%self.width]
