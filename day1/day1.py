#!/usr/bin/env python


def slice_list(data, position):
    """
    create a new list with members to add
    this list must be shorter and shorter
    ex: ops for 1 2 3 should be:
    1+2, 1+3
    2+3
    """
    return data[position+1:]

# First half (2 operands)
#with open("input") as f:
#    data = f.readlines()
#    for entry in data:
#        to_add = slice_list(data, data.index(entry))
#        for i in to_add:
#            if int(i) + int(entry) == 2020:
#                print(int(i)*int(entry))

# 3 operands
def sum_list(operands):
    sum = 0
    for i in operands:
        sum = sum + i
    return sum

with open("input") as f:
    data = f.readlines()
    for entry in data:
        operands = [0]*3
        operands[0] = int(entry)
        second_operands = slice_list(data, data.index(entry))
        for i in second_operands:
            operands[1] = int(i)
            third_operands = slice_list(second_operands, second_operands.index(i))
            for j in third_operands:
                operands[2] = int(j)
                sum = sum_list(operands)
                if sum == 2020:
                    print(operands[0] * operands[1] * operands[2])

