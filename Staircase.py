#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    decre = n
    for i in range(n+1):
        if i == 0:
            continue
        decre -= 1
        for j in reversed(range(decre)):
            print(' ', end='')
        for j in range(i):
            print('#', end='')
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
