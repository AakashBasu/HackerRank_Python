#!/bin/python3


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left_diagonal = 0
    left_diagonal = sum(arr[i][i] for i in range(n))
    right_diagonal = sum(arr[i][n-i-1] for i in range(n))
    return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    result = diagonalDifference(arr)
    print(result)

