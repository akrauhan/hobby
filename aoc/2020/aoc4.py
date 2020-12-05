import helpFunctions as hF

validfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def isFourDigitsBetween(str, min, max):
    return (len(str) == 4 and min <= int(str) and int(str) <= max)


def isValid(passport):
    passport = passport.split(" ")
    c = 0
    for field in passport:
        if field != "":
            fieldInfo = field.split(":")[1]
        field = field.split(":")[0]
        if field == "byr":
            if not isFourDigitsBetween(fieldInfo, 1920, 2002):
                return False
            c += 1
            print("Valid: ", field)
        if field == "iyr":
            if not isFourDigitsBetween(fieldInfo, 2010, 2020):
                return False
            c += 1
            print("Valid: ", field)
        if field == "eyr":
            if not isFourDigitsBetween(fieldInfo, 2020, 2030):
                return False
            c += 1
            print("Valid: ", field)
        if field == "hgt":
            unit = fieldInfo[-2:]
            size = fieldInfo[:-2]
            if unit == "in":
                if not(59 <= int(size) and int(size) < 76):
                    return False
            if unit == "cm":
                if not(150 <= int(size) and int(size) < 193):
                    return False
            c += 1
            print("Valid: ", field)
        if field == "hcl":
            if fieldInfo[0] != "#" or len(fieldInfo[1:]) != 6:
                return False
            for char in fieldInfo[1:]:
                if char in ["a", "b", 'c', "d", "e", "f"]:
                    continue
                if int(char) in range(10):
                    continue
                return False
            c += 1
            print("Valid: ", field)
        if field == "ecl":
            if fieldInfo not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            c += 1
            print("Valid: ", field)
        if field == "pid":
            if len(fieldInfo) != 9:
                return False
            for no in fieldInfo:
                if int(no) not in range(10):
                    return False
            c += 1
            print("Valid: ", field)
    return c == 7


input = hF.txt2Table("aoc4.txt")

passports = []
tmp = ""
for line in input:
    if (line == "\n"):
        passports.append(tmp)
        tmp = ""
        continue
    tmp += line.replace("\n", " ")

c = 0
for passport in passports:
    valid = isValid(passport)
    if valid:
        c += 1
    print(valid)

print("Valid passports: ", c)   # gives 1 too few??
