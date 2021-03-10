import random
from timeit import Timer


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def selectionSortSimul(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


# Performance Analysis

nonSimul, simul = 0, 0

for i in range(500):
    list1 = random.sample(range(1000), 500)
    t1 = Timer("selectionSort(list1)", "from __main__ import selectionSort,list1")
    t2 = Timer("selectionSortSimul(list1)", "from __main__ import selectionSortSimul,list1")

    nonSimul += t1.timeit(10)
    simul += t2.timeit(10)

    if i % 5 == 0:
        print("Loading: " + str(i // 5 + 1) + "%")

print("Without Simultaneous Assignment: " + str(nonSimul))
print("With Simultaneous Assignment:    " + str(simul))

# *** RESULT: No simultaneous assignment wins! ***
