import random
from timeit import Timer


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def doubleBubble(alist):
    upPasses = 0
    downPasses = 0
    # print("before sorting " + str(alist))
    for passnum in range(len(alist)):
        if passnum % 2 == 0:  # first, third, fifth, etc passes -> bubble up
            for i in range(len(alist)-upPasses-1):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            # print("after up pass " + str(alist))
            upPasses += 1
        else:  # second, fourth, sixth, etc passes -> bubble down
            for j in range(len(alist)-downPasses-1, 0, -1):
                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]
            # print("after down pass " + str(alist))
            downPasses += 1


# Performance Analysis

single, double = 0, 0

for i in range(500):
    list1 = random.sample(range(1000), 500)
    t1 = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    t2 = Timer("doubleBubble(list1)", "from __main__ import doubleBubble,list1")

    single += t1.timeit(10)
    double += t2.timeit(10)

    if i % 5 == 0:
        print("Loading: " + str(i // 5 + 1) + "%")

print("Normal Bubble Sort: " + str(single))
print("Double Bubble Sort: " + str(double))

# RESULT: Normal bubble sort wins!
