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
        """
        2 step validation
        """
        if self.global_validate():
            return self.minute_validate()
        else:
            return False


    def global_validate(self):
        """
        Field count and optional fields
        """
        if len(self.fields) == 8:
            return True
        elif 'cid' not in self.fields and len(self.fields) == 7:
            return True
        else:
            return False


    def minute_validate(self):
        """
        Validate each field precisely
        """
        validation_result = []
        for k in self.fields:
            if k == "byr":
                validation_result.append(self.year_validate(k, 4, 1920, 2002))
            elif k == "iyr":
                validation_result.append(self.year_validate(k, 4, 2010, 2020))
            elif k == "eyr":
                validation_result.append(self.year_validate(k, 4, 2020, 2030))
            elif k == "hgt":
                validation_result.append(self.height_validate(k))
            elif k == "hcl":
                validation_result.append(self.haircolor_validate(k))
            elif k == "ecl":
                validation_result.append(self.eyecolor_validate(k))
            elif k == "pid":
                validation_result.append(self.id_validate(k))
            else:
                # CID case
                pass
        if False in validation_result:
            return False
        else:
            return True

    def year_validate(self, field_name, length, lower_bound, upper_bound):
        if len(self.fields[field_name]) == length and int(self.fields[field_name]) >= lower_bound and int(self.fields[field_name]) <= upper_bound:
            return True
        else:
            return False


    def height_validate(self, field_name):
        try:
            unit = self.fields[field_name][-2:]
            if unit not in ["cm", "in"]:
                return False

            value = int(self.fields[field_name][0:-2])

            if unit == "cm" and value >= 150 and value <= 193:
                return True

            if unit == "in" and value >= 59 and value <= 76:
                return True

            return False
        except:
            print("unit:", unit)
            print("value:", value)


    def haircolor_validate(self, field_name):
        if self.fields[field_name][0] != "#":
            return False
        value = self.fields[field_name][1:]
        # Try to convert the hex into decimal to validate
        try:
            int(f"0x{value}", 16)
        except:
            return False

        return True


    def eyecolor_validate(self, field_name):
        if not self.fields[field_name] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        else:
            return True


    def id_validate(self, field_name):
        if len(self.fields[field_name]) != 9:
            return False
        else:
            return True


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

# Part 1: global validation
#passports_validation = [Passport(i).global_validate() for i in batch_import("input")]
#print(passports_validation.count(True))

# Part 2: full validation (global + minute)
passports_validation = [Passport(i).validate() for i in batch_import("input")]
print(passports_validation.count(True))
