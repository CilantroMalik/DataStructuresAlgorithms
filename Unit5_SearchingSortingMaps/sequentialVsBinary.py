from timeit import Timer
from random import randrange

"""
--- Sequential vs Binary Search ---
This program compares the performance of a sequential search and a recursive binary search
on an ordered list. It provides implementations of both of these sorting methods and then
runs a timing experiment to test their performance and how it scales with sizes of lists.
"""


# sequentially searches item by item until it either finds the item or a larger one
# this only works for an ordered list (since it has the property of being increasing)
def orderedSequentialSearch(alist, item):
    pos = 0  # keep track of current index
    found = False  # have we found the item?
    stop = False  # have we reached something larger than the item?
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:  # if the current item is equal to our target, we are done
            found = True
        else:
            if alist[pos] > item:  # if it is greater, we are also done, but not found
                stop = True
            else:  # if neither, just increase the index and keep searching
                pos = pos + 1

    return found  # will be false if we either exited through `stop` or exhausted the whole list


# splits the list in half every time by comparing the desired item to the item in the middle
# so each time it checks an item, it eliminates half the remaining items from consideration
def binarySearch(alist, item):
    if len(alist) == 0:  # base case: an empty list obviously does not contain the item
        return False
    else:
        midpoint = len(alist) // 2  # want to check the middle of the list (or as close as we can get)
        if alist[midpoint] == item:  # we have found the item --> we are done
            return True
        else:
            # recurse on either half of the list
            if item < alist[midpoint]:  # if the item is smaller than the midpoint, it is in the left half
                return binarySearch(alist[:midpoint], item)
            else:  # if greater, the item is on the right
                return binarySearch(alist[midpoint + 1:], item)


# test: run for increasing sizes of lists; use timeit.Timer for more accuracy/reproducibility
for i in range(10000, 100001, 10000):
    # create two timers that each run one of the functions
    t1 = Timer("orderedSequentialSearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,orderedSequentialSearch,list1")
    list1 = [randrange(i) for k in range(i)]
    list1.sort()

    t2 = Timer("binarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,binarySearch,list1")

    # uncomment these two lines to output length and time as points in the coordinate plane for graphing
    # print("(" + str(i / 10000) + ", " + str(t1.timeit(1000)) + ")")  # (x, y) format for graphing,   sequential
    # print("(" + str(i / 10000) + ", " + str(t2.timeit(1000)) + ")")  # (x, y) format for graphing,   binary
    print("Sequential -> Length: " + str(i) + "; Time: " + str(t1.timeit(1000)))  # verbose results, sequential
    print("Binary     -> Length: " + str(i) + "; Time: " + str(t2.timeit(1000)))  # verbose results, binary
