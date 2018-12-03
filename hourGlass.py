#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr_sum = []
    counter = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            arr_sum.append(sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
            counter += 1
    return arr_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    # print(len(arr) - 2)
    result = hourglassSum(arr)
    print(max(result))
    fptr.write(str(max(result)) + '\n')

    fptr.close()

# a = []
# for i in range(3):
#     a.append(list(map(int, input().rstrip().split())))
# # print(a[0:3])
# print(sum(a[0][0:3]) + a[1][1] + sum(a[2][0:3]))
