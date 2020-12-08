import pytest
from day7 import expand_bag, replace_expand, parse_rules, get_regex_standard, parse_expand, count_find


def test_expand_bag():
    graph = {
        "light red":["bright white", "muted yellow", "muted yellow"],
        "dark orange":["bright white", "bright white", "bright white", "muted yellow", "muted yellow", "muted yellow", "muted yellow"],
        "bright white":["shiny gold"],
        "muted yellow":["shiny gold", "shiny gold", "faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue"],
        "shiny gold":["dark olive", "vibrant plum", "vibrant plum"],
        "vibrant plum":["faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","dotted black","dotted black","dotted black","dotted black","dotted black","dotted black"],
        "faded blue":[],
        "dotted black":[]
    }

    assert True == expand_bag("bright white", graph, find="shiny gold")
    assert True == expand_bag("muted yellow", graph, find="shiny gold")
    assert False == expand_bag("faded blue", graph, find="shiny gold")

    graph = {
        "light red":["bright white", "muted yellow", "muted yellow"],
        "dark orange":["bright white", "bright white", "bright white", "muted yellow", "muted yellow", "muted yellow", "muted yellow"],
        "bright white":["shiny gold"],
        "muted yellow":["shiny gold", "shiny gold", "faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","faded blue"],
        "shiny gold":["dark olive", "vibrant plum", "vibrant plum"],
        "vibrant plum":["faded blue","faded blue","faded blue","faded blue","faded blue","faded blue","dotted black","dotted black","dotted black","dotted black","dotted black","dotted black"],
        "faded blue":[],
        "dotted black":[]
    }

    assert False == expand_bag("vibrant plum", graph, find="shiny gold")


def test_replace_expand():
    mylist = ["a", "b"]
    add = ["zz", "zz"]
    assert ["b", "zz", "zz"] == replace_expand(mylist, replace_pos=0, by=add)

    mylist = ["a", "a", "b"]
    add = ["zz", "zz"]
    assert ["a", "b", "zz", "zz"] == replace_expand(mylist, replace_pos=1, by=add)

def test_get_regex_standard():
    data = "dull plum bags contain 2 posh gray bags, 1 bright aqua bag, 3 faded lavender bags, 3 dull salmon bags."
    regex = r"(\w+ \w+) bags contain (\d \w+ \w+) bag[s]*[,.] (\d \w+ \w+) bag[s]*[,.] (\d \w+ \w+) bag[s]*[,.] (\d \w+ \w+) bag[s]*[,.]"

    assert regex == get_regex_standard(3)


def test_parse_expand():
    data = "1 dull plum"
    assert ["dull plum"] == parse_expand(data)
    data = "2 dark gray"
    assert ["dark gray", "dark gray"] == parse_expand(data)


def test_parse_rules():
    data = [
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
    ]
    assert {"faded blue": [], "dotted black": []} == parse_rules(data)

    data = [
    "bright white bags contain 1 shiny gold bag.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    ]
    assert {"bright white": ["shiny gold"], "shiny gold": ["dark olive", "vibrant plum", "vibrant plum"]} == parse_rules(data)


def test_count_find():
    data = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]

    rules = parse_rules(data)
    assert 4 == count_find(rules, "shiny gold")

    #data = [
    #    "light chartreuse bags contain 2 dull silver bags, 5 faded maroon bags, 5 drab purple bags, 5 shiny gold bags.",
    #    "striped beige bags contain 5 shiny yellow bags, 5 striped magenta bags, 1 shiny gold bag, 2 dotted tan bags.",
    #    "shiny gold bags contain no other bags.",
    #    "vibrant chartreuse bags contain 1 dim indigo bag, 1 drab purple bag, 2 shiny gold bags, 3 faded salmon bags.",
    #    "dotted lavender bags contain 2 light gold bags, 3 shiny gold bags, 3 dim tan bags.",
    #]

    #rules = parse_rules(data)
    #assert 5 == count_find(rules, "shiny gold")
