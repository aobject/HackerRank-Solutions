#!/bin/python3

# HackerRank
# Problem: Hashmaps Count Triplets
# Status: In process

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0
    all_val = dict()

    for i, item in enumerate(arr):
        if item not in all_val:
            all_val[item] = [i]
        else:
            all_val[item].append(i)

    for i in range(1, len(arr) - 1):
        if arr[i] % r:
            continue

        # count element occur before A[i] and has a value of A[i]/r
        lower_count = 0
        temp_arr = all_val[arr[i] / r]
        for j, index in enumerate(temp_arr):
            if index < i:
                lower_count += 1

        # count elements after A[i] and has a value of A[i]*r
        higher_count = 0
        temp_arr = all_val[arr[i] * r]
        for j, index in enumerate(temp_arr):
            if index > i:
                higher_count += 1

        # add the count of total possible combinations
        result += lower_count * higher_count
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
