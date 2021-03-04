from timeit import Timer
import random


def iterativeBinarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def recursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursiveBinarySearch(alist[:midpoint], item)
            else:
                return recursiveBinarySearch(alist[midpoint + 1:], item)


for i in range(10000, 100001, 10000):
    t1 = Timer("iterativeBinarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,iterativeBinarySearch,list1")
    list1 = [random.randrange(i) for k in range(i)]
    list1.sort()

    t2 = Timer("recursiveBinarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,recursiveBinarySearch,list1")

    # print("(" + str(i / 10000) + ", " + str(t1.timeit(1000)) + ")")  # (x, y) format for graphing, iterative
    # print("(" + str(i / 10000) + ", " + str(t2.timeit(1000)) + ")")  # (x, y) format for graphing, recursive
    print("Iterative -> Length: " + str(i) + "; Time: " + str(t1.timeit(1000)))  # verbose output,   iterative
    print("Recursive -> Length: " + str(i) + "; Time: " + str(t2.timeit(1000)))  # verbose output,   recursive
