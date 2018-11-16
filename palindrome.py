counter = 0
a = int(input())
arr = list(map(int, input().rstrip().split()))
if len(arr) == a:
    if all(item >= 0 for item in arr):
        for i in arr:
            if i >= 0:
                if i == int(str(i)[::-1]):
                    counter += 1
if counter >= 1:
    print(True)
else:
    print(False)
