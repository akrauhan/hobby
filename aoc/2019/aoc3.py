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
    points = []
    for i in range(0, len(wire)):
        l += 1
        if wire[i][0] == "R":
            for j in range(0, wire[i][1]):
                x += 1
                points.append((x,y,l))
        if wire[i][0] == "D":
            for j in range(0, wire[i][1]):
                y -= 1
                points.append((x,y,l))
        if wire[i][0] == "L":
            for j in range(0, wire[i][1]):
                x -= 1
                points.append((x,y,l))
        if wire[i][0] == "U":
            for j in range(0, wire[i][1]):
                y += 1
                points.append((x,y,l))
    return points

frstPoints = pointsPassed(frstWire)
scndPoints = pointsPassed(scndWire)

def tupleFromTriple(x):
    return x[0:2]

frstPointsCrdn = [tupleFromTriple(x) for x in frstPoints]
scndPointsCrdn = [tupleFromTriple(x) for x in scndPoints]
    
intersections = list(set(frstPointsCrdn).intersection(scndPointsCrdn))
distances = [ (abs(pair[0])+abs(pair[1])) for pair in intersections]
print(min(distances)) # Task 1 Correct

def indices(where, what):
    indices = []
    for x in what:
        indices.append(where.index(x))
    return indices

frstIndices = indices(frstPointsCrdn, intersections)
scndIndices = indices(scndPointsCrdn, intersections)

def lengthFromIndices(t, indices):
    lengths = []
    for i in indices:
        lengths.append(t[i][2])
    return lengths

frstLengths = lengthFromIndices(frstPoints, frstIndices)
scndLengths = lengthFromIndices(scndPoints, scndIndices)
sumLengths = frstLengths + scndLengths
print(min(sumLengths))# HECK