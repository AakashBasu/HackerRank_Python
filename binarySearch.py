arr = [a+1 for a in range(100000000)]
print(arr)

target = 99999999

from time import time

t1 = int(round(time() * 1000))
t1s = time()
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + high // 2
        if target == mid:
            return True
        elif target < mid:
            high = mid - 1
        else:
            low = mid + 1
    return False

a = binarySearch(arr, target)
print(a)

t2 = int(round(time() * 1000))
t2s = time()

print(t2 - t1, 'milli-secs.')
print(t2s - t1s, 'secs.')
