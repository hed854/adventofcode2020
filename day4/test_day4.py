import pytest
from day4 import Passport, batch_import

def test_batch_import():

    t = batch_import("test_input")
    reference = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929", "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"]
    assert reference == t

def test_passport_parse():
    p = Passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm")
    reference = {"ecl": "gry",  "pid": "860033327", "eyr":"2020", "hcl":"#fffffd", "byr":"1937", "iyr":"2017", "cid":"147", "hgt":"183cm"}
    assert reference == p.parse()

def test_passport_validate():
    p = Passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm")
    assert True == p.validate()

    p = Passport("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929")
    assert False == p.validate()

    p = Passport("hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm")
    assert True == p.validate()

    p = Passport("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in")
    assert False == p.validate()

