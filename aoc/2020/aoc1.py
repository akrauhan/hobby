import helpFunctions as hF

input = hF.txt2Table("aoc1.txt", int)

for i in input:
    for j in input:
        for k in input:
            if (i + j + k == 2020):
                print(i*j*k)
