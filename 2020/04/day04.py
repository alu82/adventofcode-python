import os

def solve(myInput):
    valid_passports_1 = 0
    valid_passports_2 = 0
    passport = ""
    for line in myInput:
        if not line:
            if checkPassport(passport):
                valid_passports_1 += 1
            if checkPassport_2(passport):
                valid_passports_2 += 1
            passport = ""
        else:
            passport += " " + line
    print(valid_passports_1)
    print(valid_passports_2)

def parse_passport(passport):
    passport_dict = {}
    pairs = passport.split(" ")
    for pair in pairs:
        if pair:
            k,v = tuple(pair.split(":"))
            passport_dict[k] = v
    return passport_dict

def checkPassport_2(passport):
    passport_dict = parse_passport(passport)
    try:
        if "byr" in passport_dict:
            byr = int(passport_dict["byr"])
            if not (1920 <= byr <= 2002):
                return False
        else:
            return False

        if "iyr" in passport_dict:
            iyr = int(passport_dict["iyr"])
            if not (2010 <= iyr <= 2020):
                return False
        else:
            return False


        if "eyr" in passport_dict:
            eyr = int(passport_dict["eyr"])
            if not (2020 <= eyr <= 2030):
                return False
        else:
            return False

        if "hgt" in passport_dict:
            hgt = passport_dict["hgt"]
            e = hgt[-2:]
            if not e in ["cm", "in"]:
                return False
            elif e == "cm":
                v = int(hgt[:-2])
                if not (150 <= v <= 193):
                    return False
            elif e == "in":
                v = int(hgt[:-2])
                if not (59 <= v <= 76):
                    return False
        else:
            return False

        if "hcl" in passport_dict:
            hcl = passport_dict["hcl"]
            if not hcl[0] == "#":
                return False
            h = hcl[1:]
            if not len(h) == 6:
                return False
            allowed = set([str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f'])
            if not allowed.issuperset(set(h)):
                return False
        else:
            return False

        if "ecl" in passport_dict:
            ecl = passport_dict["ecl"]
            if not ecl in ["amb","blu","brn","gry","grn","hzl","oth"]:
                return False
        else:
            return False

        if "pid" in passport_dict:
            pid = passport_dict["pid"]
            if not len(pid) == 9:
                return False
            int(pid)
        else:
            return False
            
    except Exception as e:
        print(e)
        return False
    return True



def checkPassport(passport):
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport_field in passport_fields:
        if not passport_field in passport:
            return False
    return True


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    input = [line.strip() for line in myInput]
    input.append("")
    solve(input)