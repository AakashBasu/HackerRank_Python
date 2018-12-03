#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastAns = 0
    arr_of_lastAns = []
    list_of_sequence = []
    for i in range(n):
        list_of_sequence.append([])
    # print(list_of_sequence)
    for arr in queries:
        # print(arr[0])
        # print(type(arr[0]))
        if arr[0] == 1:
            index = (arr[1] ^ lastAns) % n
            list_of_sequence[index].append(arr[2])
        elif arr[0] == 2:
            sequence_no = (arr[1] ^ lastAns) % n
            # print(len(list_of_sequence[sequence_no]))
            element_index = arr[2] % len(list_of_sequence[sequence_no])
            # print(element_index)
            lastAns = list_of_sequence[sequence_no][element_index]
            arr_of_lastAns.append(lastAns)
    return arr_of_lastAns


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    # print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
