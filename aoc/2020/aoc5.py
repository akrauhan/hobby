import helpFunctions as hF
import math

input = hF.txt2Table("aoc5.txt")


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def getSeat(s):
    rows = range(128)
    columns = range(8)

    for char in s[:-3]:
        if (char == "F"):
            rows = split_list(rows)[0]
        if (char == "B"):
            rows = split_list(rows)[1]

    for char in s[-4:]:
        if (char == "L"):
            columns = split_list(columns)[0]
        if (char == "R"):
            columns = split_list(columns)[1]

    return (rows[0], columns[0], rows[0]*8 + columns[0])


def getMySeat(seats):
    validseats = []
    for i in range(1, len(seats) - 1):
        for j in range(1, len(seats)-1):
            diff = seats[i][2] - seats[j][2]
            if abs(diff) == 2:
                validseats.append(min(seats[i][2], seats[j][2])+1)

    return validseats


def getMissingSeats(seats):
    possibleseatIDs = []

    for i in range(128):
        for j in range(8):
            possibleseatIDs.append(8*j+i)

    myPossibleSeat = getMySeat(seats)

    return (list(set(possibleseatIDs) & set(myPossibleSeat)))


seatIDs = []
seats = []
for seat in input:
    rowcolid = getSeat(seat)
    seatIDs.append(rowcolid[2])
    seats.append(rowcolid)
    print(rowcolid)
print(max(seatIDs))
print(getMissingSeats(seats))
