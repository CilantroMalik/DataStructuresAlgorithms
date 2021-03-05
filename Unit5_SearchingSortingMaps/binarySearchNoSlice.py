from timeit import Timer
import random

"""
--- Binary Search Without Slice Operator ---

"""


# refer to exercise "recursiveVsIterative" for a full overview of this method with comments
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


# similar to above: this is the same implementation as the one offered and discussed in another exercise
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


# for the new implementation: use a wrapper function since we need a few extra parameters
def binarySearchNoSlice(alist, item):
    return binarySearchNoSliceHelper(alist, item, 0, len(alist)-1)


# pass in the list and item as normal, plus the start and end indices as parameters since we cannot modify the list itself
def binarySearchNoSliceHelper(alist, item, start_index, end_index):
    if end_index - start_index == -1:  # check whether the end and start indices overlap
        return False  # this means the item is not in the list (base case)
    else:
        # end - start - 1 will be the length of the relevant part of the list; divide this by 2 to get
        # the offset of the midpoint from the start of the list; then add the start index to get the position
        # of this midpoint with respect to the whole list
        midpoint = ((end_index - start_index + 1) // 2) + start_index
        if alist[midpoint] == item:  # if we have found the item at this inde, we are done
            return True
        else:
            if item < alist[midpoint]:  # if the item is less than the midpoint, it is in the left half, so alter the indices
                return binarySearchNoSliceHelper(alist, item, start_index, midpoint-1)  # only care about items before midpoint
            else:  # if the item is greater, it is in the right half, so change the indices to look at items after midpoint
                return binarySearchNoSliceHelper(alist, item, midpoint+1, end_index)


# same timing procedure as in earlier exercises, just with three timers for the three methods and larger test lists
for i in range(100000, 1000001, 100000):
    t1 = Timer("binarySearchNoSlice(list1, random.randrange(%d))" % i,
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
    print("-------------------------------------------------------")
