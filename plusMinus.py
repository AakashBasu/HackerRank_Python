#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = sum(x > 0 for x in arr)
    neg = sum(x < 0 for x in arr)
    zero = sum(x == 0 for x in arr)
    print('{0:.6f}'.format(pos/n), '{0:.6f}'.format(neg/n), '{0:.6f}'.format(zero/n), sep='\n')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    plusMinus(arr)
