#!/usr/bin/env python
"""
advent of code 2020 day 7: Handy Haversacks
https://adventofcode.com/2020/day/7
"""
import re

class ColoredString():
    def __init__(self):
        self.reset = "\033[0m"
    def red(self, text):
        red = "\033[0;31m"
        return(f"{red}{text}{self.reset}")
    def yellow(self, text):
        red = "\033[0;33m"
        return(f"{red}{text}{self.reset}")

def expand_bag(color, rules, find):
    """
    Choose one bag color to expand according to provided rules
    Return True if a <find> bag is found
    """

    c = ColoredString()
    def debug_bag(color,data):
        debug_string=f"{color}:"
        for i in data:
            if i == "shiny gold":
                debug_string = debug_string + c.yellow('O')
            else:
                debug_string = debug_string + c.red('.')
        return debug_string
    # create a working copy
    rules_copy = rules.copy()
    # Isolate the target bag
    colors_to_expand = rules_copy.pop(color)

    # Numerical index (because there are dupes)
    for i in range(len(colors_to_expand)):
        # at each iteration, check if we found the gold bag
        if find in colors_to_expand:
            #print(debug_bag(color, colors_to_expand))
            return True
        if len(rules_copy[colors_to_expand[i]]) != 0:
            # pseudo-replace
            colors_to_expand = replace_expand(colors_to_expand, replace_pos=i, by=rules_copy[colors_to_expand[i]])
        else:
            # empty bags
            pass
    # i've expanded the whole bag and all i got is this lousy result
    #print(debug_bag(color, colors_to_expand))
    return False


def replace_expand(target, replace_pos, by):
    """
    Replace any position of the list by another list
    Order is messed up
    """
    target.extend(by)
    del(target[replace_pos])
    return target


def parse_expand(expression):
    """
    Input your "X foo bar" expression
    And get your customized list in output
    """
    parsed = expression.split(" ")
    expanded = []
    color = " ".join(parsed[1:])
    expanded.extend([color]*int(parsed[0]))
    return expanded


def get_regex_empty():
    return r"(\w+ \w+) bags contain (no other bags)"


def get_regex_standard(comma_count):
    part1 = r"(\w+ \w+) bags contain "
    part2 = [r"(\d \w+ \w+) bag[s]*[,.]"] * (comma_count + 1)
    return part1 + " ".join(part2)


def parse_rules(data):
    rules = {}
    for line in data:
        # check if bag has no contents
        r = re.compile(get_regex_empty())
        match = r.match(line)
        if match and match.group(2):
            rules[match.group(1)] = []
        else:
            # if bags does have contents, calculate the parametric regex
            comma_count=len(re.compile(r",").findall(line))
            r = re.compile(get_regex_standard(comma_count))
            match = r.findall(line)
            data = []
            # first match is the color
            # Use a list because we can't pop tuples
            matchlist = list(match[0])
            color = matchlist.pop(0)
            # other must be expanded
            for i in matchlist:
                data.extend(parse_expand(i))
            rules[color] = data
    return rules


def count_find(rules, find):
    count = 0
    for color in rules:
        if expand_bag(color, rules, find):
            count = count + 1
    return count

with open("input") as file:
    rules = parse_rules(file)
    count = count_find(rules, "shiny gold")
    print(f"{count} bags can contain shiny gold")
