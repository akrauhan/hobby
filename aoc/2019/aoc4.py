# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:13:09 2019

@author: akrauhan
"""

lowerLimit = 172851
upperLimit = 675869

def isValid(number):
    digits = [int(i) for i in str(number)]
    twoAdjacent = False
    po1 = 0 # Pointer 1
    po2 = 1 # Pointer 2
    
    while (po2 < len(digits)):
        if digits[po1] == digits[po2]: 
            twoAdjacent = True
        if digits[po1] > digits[po2]: return False
        po1+=1
        po2+=1
    return twoAdjacent

def validDigitsBetween(lower, upper):
    count = 0
    for i in range(lower, upper):
        if (isValid(i)): count+=1
    return count

#print(validDigitsBetween(lowerLimit,upperLimit)) #Part 1 Correct

def isValid2(number):
    digits = [int(i) for i in str(number)]
    
    po1 = 0 # Pointer 1
    po2 = 1 # Pointer 2
    adjacentCount =  {i: 0 for i in range(0,10)}
    while (po2 < len(digits)):
        if digits[po1] > digits[po2]: return False
        if digits[po1] == digits[po2]: 
            adjacentCount[digits[po1]] += 1
        po1+=1
        po2+=1
        
    for entry in adjacentCount:
        if adjacentCount[entry] == 1: return True
    
    return False
        
print(isValid2(123444))

def validDigitsBetween2(lower, upper):
    count = 0
    for i in range(lower, upper):
        if (isValid2(i)): count+=1
    return count

print(validDigitsBetween2(lowerLimit, upperLimit)) # Part 2 Correct