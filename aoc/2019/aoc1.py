# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:09:39 2019

@author: akrauhan
"""
import math
from helpFunctions import txt2Table

puzzleInput = txt2Table("aoc1.txt", int)

def fuelForModule(m):
    '''Fuel for module with mass of m.'''
    return math.floor(m/3) - 2

fuels = map(fuelForModule, puzzleInput)
sumOfFuels = sum(fuels)

print(sumOfFuels) # Task 1 correct.

def fuelForFuel(m):
    '''Fuel for module or fuel with mass m'''
    mbyFuelMass = math.floor(m/3) - 2
    if (mbyFuelMass <= 0): return 0
    return mbyFuelMass + fuelForFuel(mbyFuelMass)

fuels2 = map(fuelForFuel, puzzleInput)
sumOfFuels2 = sum(fuels2)

print(fuelForFuel(14)) ## Test: 2
print(fuelForFuel(48)) ## Test: 16
print(fuelForFuel(1969)) ## Test: 966

print(sumOfFuels2) # Task 2 correct.