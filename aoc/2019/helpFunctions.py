# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:41:50 2019

Apufunktiota tiedostojen lukemiseen.
Luotu Advent of Code varten.

@author: akrauhan
"""

def txt2Table(filename, oType):
    '''Takes filename of text-file with strings, returns table parsed with type given.'''
    
    parseType = oType
    if (oType == "string"): parseType = str
    elif (oType == "integer"): parseType = int
    elif (oType == "double"): parseType = float
            
    file = open(filename,"r")
    t = []
    for line in file:
        t.append(parseType(line))
    file.close()
    return t

def txt2StrTable(filename):
    '''Takes filename of text-file with string on each line, returns stringtable with lines as elements.'''
    file = open(filename,"r")
    t = []
    for line in file:
        t.append(line)
    file.close()
    return t

def txt2IntTable(filename):
    '''Takes filename of text-file with strings on each line, returns parsed int table with lines as elements.'''
    file = open(filename,"r")
    t = []
    for line in file:
        t.append(int(line))
    file.close()
    return t