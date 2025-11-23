#!/bin/python3

import os
import sys

def _demo_test():
    input_data = """9
10 20 20 10 10 30 50 10 20
"""
    return input_data.strip().split('\n')

def sockMerchant(n, ar):
    unmatched = set()
    pairs = 0

    for color in ar:
        if color in unmatched:
            unmatched.remove(color)
            pairs += 1
        else:
            unmatched.add(color)

    return pairs


if __name__ == '__main__':
    # output_path = os.environ.get('OUTPUT_PATH')
    # fptr = open(output_path, 'w') if output_path else sys.stdout
    fptr = sys.stdout


    # n = int(input().strip())
    # ar = list(map(int, input().rstrip().split()))

    demo_lines = _demo_test()
    n = int(demo_lines[0].strip())
    ar = list(map(int, demo_lines[1].strip().split()))
    
    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    print(f"Expected 3 got {result}")
    
    if fptr is not sys.stdout:
        fptr.close()
