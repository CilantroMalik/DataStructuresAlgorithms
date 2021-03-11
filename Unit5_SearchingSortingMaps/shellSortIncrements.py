import math
import random
from timeit import Timer


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        # print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2


def shellSortNewIncrements(alist):
    # finding the greatest Mersenne number less than len(alist)
    sublistcount = int(math.pow(2, int(math.log(len(alist), 2)))) - 1
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        # print("After increments of size", sublistcount, "The list is", alist)

        # making the next lower Mersenne number: add 1 -> perfect power of 2, then divide by 2 and subtract one to
        # make it a Mersenne number again [started with 2^k - 1 --> ending with 2^(k-1) - 1]
        sublistcount = (sublistcount + 1) // 2 - 1


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


# Performance Analysis

original, new = 0, 0

for i in range(500):
    list1 = random.sample(range(1000), 500)
    t1 = Timer("shellSort(list1)", "from __main__ import shellSort,list1")
    t2 = Timer("shellSortNewIncrements(list1)", "from __main__ import shellSortNewIncrements,list1")

    original += t1.timeit(10)
    new += t2.timeit(10)

    if i % 5 == 0:
        print("Loading: " + str(i // 5 + 1) + "%")

print("Original Increments: " + str(original))
print("New Increments:      " + str(new))

# *** RESULT: New increment scheme (Mersenne numbers) wins! ***
