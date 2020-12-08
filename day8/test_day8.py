import pytest
from day8 import GameConsole

def test_parse_op():
    g = GameConsole([])
    instruction = {"op": "nop", "arg": 0, "exec": False}
    assert instruction == g.parse_instruction("nop +0")
    instruction = {"op": "acc", "arg": 6, "exec": False}
    assert instruction == g.parse_instruction("acc +6")
    instruction = {"op": "jmp", "arg": -96, "exec": False}
    assert instruction == g.parse_instruction("jmp -96")

def test_boot():
    # exit by loop
    g = GameConsole("test_input")
    g.boot()
    assert 5 == g.accumulator
    # exit by eof
    g = GameConsole("test_input_eof")
    g.boot()
    assert 8 == g.accumulator

def test_auto_boot():
    g = GameConsole("test_input")
    g.auto_boot()
    assert 8 == g.accumulator
