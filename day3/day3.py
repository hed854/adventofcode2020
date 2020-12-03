#!/usr/bin/env python
"""
Advent of Code 2020 Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3
"""

class ColoredString():
    def red(self, text):
        red = "\033[0;31m"
        reset = "\033[0m"
        return(f"{red}{text}{reset}")


class Map():
    """
    Map object
    - coordinates start on top left
    - is structured in layers
        * base_layer: the basic input map, read-only
        * display_layer: for any modifications. Displayed in red.
    """
    def __init__(self, input_file):
        with open(input_file) as f:
            # Since these are list of strings, it's important we remove the pesky newline
            self.base_layer = [line.rstrip("\n") for line in f]
        self.height = len(self.base_layer)
        self.width = len(self.base_layer[0])
        # create a new modifiable map layer (base_layer strings are immutable)
        # note: creating the empty list like this:
        #   self.display_layer = [[None]*self.width]*self.height]
        # creates multiple references of itself instead of copies -_-
        self.display_layer = [[None for x in range(self.width)] for x in range(self.height)]

    def get_tile(self, x, y):
        # wrap the map width
        return self.base_layer[y][x%self.width]

    def set_tile(self, x, y, value):
        # same, but for the display layer
        self.display_layer[y][x%self.width] = value

    def display(self):
        c = ColoredString()
        for i in range(self.height):
            for j in range(self.width):
                if self.display_layer[i][j] is not None:
                    print(c.red(self.display_layer[i][j]), end="")
                else:
                    print(self.base_layer[i][j], end="")
            print()

class TobogganDrive():
    """
    Let's drive into trees
    """
    def __init__(self, map, run_vector):
        self.map = map
        self.start_position = [0,0]
        self.run_vector = run_vector
        self.crashed_in_tree = 0

    def run(self):
        position = self.start_position
        # Go to the bottom of the map
        while position[1] < self.map.height:
            tile = self.map.get_tile(position[0], position[1])
            if tile == "#":
                self.crashed_in_tree = self.crashed_in_tree + 1
                self.map.set_tile(position[0], position[1], "X")
            else:
                self.map.set_tile(position[0], position[1], "0")
            position = [position[0] + self.run_vector[0], position[1] + self.run_vector[1]]
        return self.crashed_in_tree

# First half
t = TobogganDrive(Map("input"), [3,1])
a_run = t.run()
print(f"Slope {t.run_vector} => Crashed {a_run} times")

# Second half
t = TobogganDrive(Map("input"), [1,1])
b_run = t.run()
print(f"Slope {t.run_vector} => Crashed {b_run} times")

t = TobogganDrive(Map("input"), [5,1])
c_run = t.run()
print(f"Slope {t.run_vector} => Crashed {c_run} times")

t = TobogganDrive(Map("input"), [7,1])
d_run = t.run()
print(f"Slope {t.run_vector} => Crashed {d_run} times")

t = TobogganDrive(Map("input"), [1,2])
e_run = t.run()
print(f"Slope {t.run_vector} => Crashed {e_run} times")

print(a_run * b_run * c_run * d_run * e_run)
