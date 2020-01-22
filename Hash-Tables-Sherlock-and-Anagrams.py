#!/bin/python3

# HackerRank
# Problem: Hash Tables Sherlock and Anagrams


import math
import os
import random
import re
import sys

def makeSignature(s):
    result = []
    resultStr = ''

    for i in range(26): result.append(0)

    for i in range(len(s)):
        result[ord(s[i]) - ord('a')] += 1

    for i in range(26):
        resultStr += str(result[i])
    return resultStr

# Complete the sherlockAndAnagrams function below.
# input: one strings
# output: int number of anagrams
def sherlockAndAnagrams(s):
    # go through all possible sub strings
    sigList = []
    for i in range(len(s)):
        j = i
        while j >= 0:
            sigList.append(makeSignature(s[j:i+1]))
            j -= 1
    # add signature of all substrings to a list of substring signatures

    # go through all signatures checking for matches using a dictionary to count
    sigCount = dict()
    for i in range(len(sigList)):
        if sigList[i] in sigCount:
            sigCount[sigList[i]] += 1
        else:
            sigCount[sigList[i]] = 1
    # summation rule tells us n values has n*(n-1)/2 possible combination/anagrams
    totalSum = 0
    for i,item in enumerate(sigCount):
        n = sigCount[item]
        print('item is {}. item count is {}. addition to sum is {}.'.format(item,n,(n*(n-1)/2)))
        totalSum += (n*(n-1)/2)
    # add all summations together and return result
    return int(totalSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
