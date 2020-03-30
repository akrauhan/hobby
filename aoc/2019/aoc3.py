# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:19:19 2019

@author: akrauhan
"""
from helpFunctions import txt2Table

def str2Tuple(string):
    return (string[0], string[1:])

wiresAsStrings = txt2Table("aoc3.txt")
frstWireUnsplit = wiresAsStrings[0].split(",")
scndWireUnsplit = wiresAsStrings[1].split(",")

frstWire = [(x[0], int(x[1:])) for x in frstWireUnsplit]
scndWire = [(x[0], int(x[1:])) for x in scndWireUnsplit]
    
def pointsPassed(wire):
    x = 0
    y = 0
    l = 0
    points = {}
    for i in range(0, len(wire)):
        if wire[i][0] == "R":
            for j in range(0, wire[i][1]):
                x += 1
                l += 1
                points[(x,y)] = l
        if wire[i][0] == "D":
            for j in range(0, wire[i][1]):
                y -= 1
                l += 1
                points[(x,y)] = l
        if wire[i][0] == "L":
            for j in range(0, wire[i][1]):
                x -= 1
                l += 1
                points[(x,y)] = l
        if wire[i][0] == "U":
            for j in range(0, wire[i][1]):
                y += 1
                l += 1
                points[(x,y)] = l
    return points

frstPoints = pointsPassed(frstWire)
scndPoints = pointsPassed(scndWire)
both = set(frstPoints.keys())&set(scndPoints.keys())

part1 = min([abs(x) + abs(y) for (x,y) in both])
part2 = min([frstPoints[p]+scndPoints[p] for p in both])

print(part1, part2)