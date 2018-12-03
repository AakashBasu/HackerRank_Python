# from random import shuffle
# x = [i for i in range(10)]
# shuffle(x)

x = [7, 1, 4, 2, 5, 9, 8, 3, 6, 0]
print(x)

def bubbleSort(x):
    for i in range(len(x) - 1):
        for j in range(len(x) - 1 - i):
            # print(x)
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

sorted_x = bubbleSort(x)
print(sorted_x)

