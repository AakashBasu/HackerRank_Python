arr = [a+1 for a in range(100000000)]
print(arr)

target = 99999999

from time import time

t1 = int(round(time() * 1000))
t1s = time()
def linearSearch(arr, target):
    for n in range(len(arr)):
        if arr[n] == target:
            return True
    return False

a = linearSearch(arr, target)
print(a)

t2 = int(round(time() * 1000))
t2s = time()


print(t2 - t1, 'milli-secs.')
print(t2s - t1s, 'secs.')
