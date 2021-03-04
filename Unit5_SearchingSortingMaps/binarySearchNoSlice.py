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


def binarySearchSlice(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchSlice(alist[:midpoint], item)
            else:
                return binarySearchSlice(alist[midpoint + 1:], item)


def binarySearchNoSlice(alist, item):
    return binarySearchHelper(alist, item, 0, len(alist)-1)


def binarySearchNoSliceHelper(alist, item, start_index, end_index):
    if end_index - start_index == -1:
        return False
    else:
        midpoint = ((end_index - start_index + 1) // 2) + start_index
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchNoSliceHelper(alist, item, start_index, midpoint-1)
            else:
                return binarySearchNoSliceHelper(alist, item, midpoint+1, end_index)


for i in range(100000, 1000001, 100000):
    t1 = Timer("binarySearchNoSLice(list1, random.randrange(%d))" % i,
               "from __main__ import random,binarySearchNoSlice,list1")
    list1 = [random.randrange(i) for k in range(i)]
    list1.sort()

    t2 = Timer("binarySearchSlice(list1, random.randrange(%d))" % i,
               "from __main__ import random,binarySearchSlice,list1")

    t3 = Timer("iterativeBinarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,iterativeBinarySearch,list1")

    # print("(" + str(i / 10000) + ", " + str(t1.timeit(1000)) + ")")  # (x, y) format for graphing,  no slice
    # print("(" + str(i / 10000) + ", " + str(t2.timeit(1000)) + ")")  # (x, y) format for graphing,  slice
    # print("(" + str(i / 10000) + ", " + str(t3.timeit(1000)) + ")")  # (x, y) format for graphing,  iterative
    print("No Slice  -> Length: " + str(i) + "; Time: " + str(t1.timeit(1000)))  # verbose output,    no slice
    print("Slice     -> Length: " + str(i) + "; Time: " + str(t2.timeit(1000)))  # verbose output,    slice
    print("Iterative -> Length: " + str(i) + "; Time: " + str(t3.timeit(1000)))  # verbose output,    iterative
