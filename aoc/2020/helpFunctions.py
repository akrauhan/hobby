# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:41:50 2019

Apufunktiota tiedostojen lukemiseen.
Luotu Advent of Code varten.

@author: akrauhan
"""
import urllib.request


def txt2Table(filename, oType=str):
    '''Takes filename of text-file with strings,
    returns table parsed with type given.'''

    file = open(filename, "r")
    t = []
    for line in file:
        t.append(oType(line))
    file.close()
    return t

def txt2Array(filename, oType=str):
    file = open(filename, "r")
    t = []
    for line in file:
        t.append(oType(line))
    file.close()
    return t

def txt2StrTable(filename):
    '''Takes filename of text-file with string on each line,
    returns stringtable with lines as elements.'''
    file = open(filename, "r")
    t = []
    for line in file:
        t.append(line)
    file.close()
    return t


def txt2IntTable(filename):
    '''Takes filename of text-file with strings on each line,
    returns parsed int table with lines as elements.'''
    file = open(filename, "r")
    t = []
    for line in file:
        t.append(int(line))
    file.close()
    return t


def url2Array(urlname, oType=str):
    '''Gets the puzzle input from URL'''
    file = urllib.request.urlretrieve(urlname)
    t = []
    for line in file:
        decoded_line = line.decode("utf-8")
        t.append(str(decoded_line))
    return t
