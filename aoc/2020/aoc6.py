import helpFunctions as hF

input = hF.txt2Table("aoc6.txt")

answers = []
tmp = ""
for line in input:
    line.replace("\n", "")
    if (line == ""):
        answers.append(tmp)
        tmp = ""
        continue
    tmp += line

if tmp != "": 
    answers.append(tmp)
print(answers)


def getDiffAnsCount(answers):
    diffanswers = set()
    for a in answers:
        if a != " " and a != "\n":
            diffanswers.add(a)
    # print(diffanswers, len(diffanswers))
    return len(diffanswers)


def getSameAnsCount(answers):
    count = 0
    for group in answers:
        group = group.split(" ")
        anscount = len(group)

        print(group)

        answercount = {}
        for answersheet in group:
            for answer in answersheet:
                if answer in answercount:
                    answercount[answer] += 1
                else:
                    answercount[answer] = 1
        print(answercount)

        
        for key in answercount:
            if answercount[key] == anscount: 
                count += 1
        
    return count


sum = 0
for a in answers:
    sum += getDiffAnsCount(a)

print("Diff answers: ", sum)

print(getSameAnsCount(answers))
