#!/usr/bin/env python
"""
advent of code 2020 day 8: Handheld Halting
https://adventofcode.com/2020/day/8
"""
import re
import time

class GameConsole():
    def __init__(self, input):
        # load instructions
        if type(input) == str:
            with open(input) as f:
                self.instructions = f.readlines()
        elif type(input) == list:
            self.instructions = input
        else:
            pass
        # state storage
        self.accumulator = 0
        self.opcodes = [self.parse_instruction(i) for i in self.instructions]

    def boot(self, alt_opcodes=None, delay=None):
        position = 0;
        opcodes = alt_opcodes or self.opcodes
        eof = len(opcodes) - 1
        current = {}
        running = True
        exit_code = None
        while running:
            try:
                current = opcodes[position]
                print(f"pos={position}, cur={current}")
                # loop detection => exit
                if current["exec"] == True:
                    exit_code = -1
                    running = False
                    break
                if current["op"] == "acc":
                    self.accumulator = self.accumulator + current["arg"]
                    opcodes[position]["exec"] = True
                    position = position + 1
                elif current["op"] == "jmp":
                    opcodes[position]["exec"] = True
                    position = position + current["arg"]
                else:
                    # nop instruction
                    opcodes[position]["exec"] = True
                    position = position + 1
                if delay:
                    time.sleep(delay)
                if position > eof:
                    exit_code = 1
                    running = False
                    break
            except:
                print(f"pos={position}, cur={current}")
        return exit_code

    def parse_instruction(self, instruction):
        r = re.compile(r"(\w{3}) ([+-]\d+)")
        match = r.findall(instruction)
        return {"op": match[0][0], "arg": int(match[0][1]), "exec": False}


    def auto_boot(self):
        """
        Try to modify the boot sequence
        """
        i = 0
        while i <= len(self.opcodes) - 1:
            working_copy = self.opcodes.copy()
            if working_copy[i]["op"] == "jmp":
                print(f"""modify {working_copy[i]["op"]} pos {i}""")
                working_copy[i]["op"] = "nop"
                res = self.boot(alt_opcodes=working_copy)
            elif working_copy[i]["op"] == "nop":
                print(f"""modify {working_copy[i]["op"]} pos {i}""")
                working_copy[i]["op"] = "jmp"
                res = self.boot(alt_opcodes=working_copy)
            i = i + 1
            if 0 == res:
                return
            else:
                continue

# First part
#g = GameConsole("input")
#g.boot()
#print(g.accumulator)

# Try to restore boot code
#g = GameConsole("input")
#    for i in g.opcodes:
#t = g.boot()
#print(t)
