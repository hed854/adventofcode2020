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

def test_passport_global_validate():
    p = Passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm")
    assert True == p.global_validate()

    p = Passport("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929")
    assert False == p.global_validate()

    p = Passport("hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm")
    assert True == p.global_validate()

    p = Passport("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in")
    assert False == p.global_validate()


def test_passport_year_validate():
    p = Passport("byr:2002 iyr:2011 eyr:2022")
    assert True == p.year_validate("byr", 4, 1920, 2002)
    assert True == p.year_validate("iyr", 4, 2010, 2020)
    assert True == p.year_validate("eyr", 4, 2020, 2030)

    p = Passport("byr:1900 iyr:2001 eyr:2080")
    assert False == p.year_validate("byr", 4, 1920, 2002)
    assert False == p.year_validate("iyr", 4, 2010, 2020)
    assert False == p.year_validate("eyr", 4, 2020, 2030)


def test_passport_height_validate():
    p = Passport("hgt:60in")
    assert True == p.height_validate("hgt")
    p = Passport("hgt:190cm")
    assert True == p.height_validate("hgt")
    p = Passport("hgt:190in")
    assert False == p.height_validate("hgt")
    p = Passport("hgt:190")
    assert False == p.height_validate("hgt")


def test_passport_haircolor_validate():
    p = Passport("hcl:#123abc")
    assert True == p.haircolor_validate("hcl")
    p = Passport("hcl:#123abz")
    assert False == p.haircolor_validate("hcl")
    p = Passport("hcl:123abz")
    assert False == p.haircolor_validate("hcl")


def test_passport_eyecolor_validate():
    p = Passport("ecl:brn")
    assert True == p.eyecolor_validate("ecl")
    p = Passport("ecl:wat")
    assert False == p.eyecolor_validate("ecl")


def test_passport_id_validate():
    p = Passport("pid:000000001")
    assert True == p.id_validate("pid")
    p = Passport("pid:0123456789")
    assert False == p.id_validate("pid")

def test_passport_minute_validate():
    p = Passport("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
    assert False == p.minute_validate()
    p = Passport("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946")
    assert False == p.minute_validate()
    p = Passport("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
    assert False == p.minute_validate()
    p = Passport("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007")
    assert False == p.minute_validate()
    p = Passport("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f")
    assert True == p.minute_validate()
    p = Passport("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
    assert True == p.minute_validate()
    p = Passport("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022")
    assert True == p.minute_validate()
    p = Passport("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")
    assert True == p.minute_validate()
