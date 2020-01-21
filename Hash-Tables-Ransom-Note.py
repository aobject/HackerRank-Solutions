#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # create dict of note with letter: letter count
    mag = dict()
    matchCount = 0
    for i, item in enumerate(magazine):

        if item in mag:
            mag[item] += 1
        else: 
            mag[item] = 1

    # iterate through magazine using hash table to keep count and check if solution found
    i = 0
    noMatch = False
    for i, item in enumerate(note):
        if item in mag:
            mag[item] -= 1
            if mag[item] < 0:
                print('No')
                return 'No'
        else:
            print('No')
            return 'No'
    print('Yes')
    return 'Yes'

        
    


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
