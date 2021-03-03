from timeit import Timer
import random


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


for i in range(10000, 100001, 10000):
    t1 = Timer("orderedSequentialSearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,orderedSequentialSearch,list1")
    list1 = [random.randrange(i) for k in range(i)]
    list1.sort()

    t2 = Timer("binarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,binarySearch,list1")

    # uncomment these two lines to output length and time as points in the coordinate plane for graphing
    # print("(" + str(i / 10000) + ", " + str(t1.timeit(1000)) + ")")  # (x, y) format for graphing,   sequential
    # print("(" + str(i / 10000) + ", " + str(t2.timeit(1000)) + ")")  # (x, y) format for graphing,   binary
    print("Sequential -> Length: " + str(i) + "; Time: " + str(t1.timeit(1000)))  # verbose results, sequential
    print("Binary     -> Length: " + str(i) + "; Time: " + str(t2.timeit(1000)))  # verbose results, binary
