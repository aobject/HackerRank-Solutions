# HackRank
# Problem: Counting Valleys

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleySum = 0
    inValley = False
    prevLoc = 0

    for i in range(n):
        curLoc = prevLoc
        if s[i] == 'U':
            curLoc += 1
        else: 
            curLoc -= 1
        
        if prevLoc == -1 and curLoc == 0:
            valleySum += 1

        prevLoc = curLoc
    return valleySum

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
