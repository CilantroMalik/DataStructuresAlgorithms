import random
from timeit import Timer


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def bubbleSortSimul(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


# Performance Analysis

nonSimul, simul = 0, 0

for i in range(1000):
    list1 = random.sample(range(1000), 500)
    t1 = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    t2 = Timer("bubbleSortSimul(list1)", "from __main__ import bubbleSortSimul,list1")

    nonSimul += t1.timeit(10)
    simul += t2.timeit(10)

    if i % 10 == 0:
        print("Loading: " + str(i // 10 + 1) + "%")

print("Without Simultaneous Assignment: " + str(nonSimul))
print("With Simultaneous Assignment:    " + str(simul))

# *** RESULT: Simultaneous assignment wins! ***
