#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    if not s:
        return 0
    length = len(s)
    a_in_s = 0
    for ch in s:
        if ch == 'a':
            a_in_s += 1

    full_repeats = n // length
    remainder = n % length

    total = a_in_s * full_repeats

    for ch in s[:remainder]:
        if ch == 'a':
            total += 1

    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()