#!/bin/python3

import os
import sys

def hourglassSum(arr):
	max_sum = -float('inf')

	for r in range(4):
		for c in range(4):
			top = arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
			mid = arr[r + 1][c + 1]
			bottom = arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
			hg_sum = top + mid + bottom
			if hg_sum > max_sum:
				max_sum = hg_sum

	return max_sum


if __name__ == '__main__':
	fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')

	arr = []

	for _ in range(6):
		arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

	result = hourglassSum(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
