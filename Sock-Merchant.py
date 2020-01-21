# HackerRank 
# Problem: Sock Merchant

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # declare variables
    totalPairs = 0
    sockPile = dict()
    # loop through all socks
    for i in range(n):
        # check if sock type is in dict and if value is 1
        if ar[i] in sockPile and sockPile[ar[i]] == 1:
            totalPairs += 1
            sockPile[ar[i]] = 0
        else: sockPile[ar[i]] = 1
    return totalPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
