# HakerRank
# Problem: Repeated String

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if n == 0 or len(s) == 0: return 0
    # make counter and while loop
    # check string with modulo
    afound = 0
    counter = 0

    loops = n // len(s)
    extra = n % len(s)

    if loops >= 1:
        for i in range(len(s)):
            if s[counter % len(s)] =='a':
                afound += 1
            counter += 1
    
    afound *= loops
    counter *= loops

    for i in range(extra):
        if s[counter % len(s)] =='a':
            afound += 1
        counter += 1

    return afound

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
