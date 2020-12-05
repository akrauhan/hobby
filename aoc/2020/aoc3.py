import helpFunctions as hF

input = hF.txt2Table("aoc3.txt")


def treesWhenSlope(right, down):
    c = 0
    row = 0
    col = 0
    row_length = len(input[0])

    while (row < len(input)):
        if (input[row][col] == "#"):
            c += 1

        row += down
        col = (col + right) % (row_length - 1)
    print("Right " + str(right) + ", Down ", str(down), ":", c)
    return(c)


prod = 1
prod *= treesWhenSlope(1, 2)
for i in range(1, 8, 2):
    prod *= treesWhenSlope(i, 1)

print(prod)
