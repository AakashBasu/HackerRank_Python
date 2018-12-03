def addAllUsingRecursion(x):
    if x == 0:
        return 0
    else:
        # print(x)
        return x + addAllUsingRecursion(x-1)

n = addAllUsingRecursion(10)
print(n)


def factorialRecursive(x):
    if x == 0:
        return 1
    else:
        return x * factorialRecursive(x-1)

n = factorialRecursive(4)
print(n)
