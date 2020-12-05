import helpFunctions as hF


def isValid(password):
    password = password.split(":")
    rules = password[0].split("-")
    min = int(rules[0])
    req = rules[1][-1]
    max = int(rules[1][:-1])

    counter = 0
    for c in password[1]:
        if c == req:
            counter += 1

    return(min <= counter and counter <= max)


def isValid2(password):
    password = password.split(":")
    rules = password[0].split("-")
    first = int(rules[0])
    req = rules[1][-1]
    last = int(rules[1][:-1])

    c = 0
    for i in (first, last):
        if password[1][i] == req:
            c += 1

    return (c == 1)


input = hF.txt2Table("aoc2.txt")

print(isValid2("9-12 q: qqqqqpqrqqlcq"))
print(isValid2("2-3 r: vxnw"))

counter = 0
for pw in input:
    if isValid2(pw):
        counter += 1

print(counter)
