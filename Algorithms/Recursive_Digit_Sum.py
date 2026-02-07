#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def get_sum_of_digits(number_string):
    return sum(int(digit) for digit in number_string)

def recursive_super_digit(current_value_str):
    if len(current_value_str) == 1:
        return int(current_value_str)
        
    new_sum = get_sum_of_digits(current_value_str)

    return recursive_super_digit(str(new_sum))


def superDigit(n, k):
    initial_sum = get_sum_of_digits(n) * k
    result = recursive_super_digit(str(initial_sum))
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
