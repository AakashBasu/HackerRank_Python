#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sum = []
    for i in arr:
        arr_sum.append(sum(arr) - i)
    print(min(arr_sum), max(arr_sum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
