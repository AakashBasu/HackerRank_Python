#!/bin/python3

import os
import sys


def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = 0
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    if ar_count == len(ar):

        result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
