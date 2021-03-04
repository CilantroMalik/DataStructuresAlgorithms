from timeit import Timer
import random

"""
--- Recursive vs Iterative Binary Search ---
Program that compares the recursive and iterative implementations of binary search in timed tests
to see which is more efficient for increasingly large test lists. Implements both methods and then
runs a timed test to display the two functions' results and compare their efficiency.
"""


# splits the list in half every time by comparing the desired item to the item in the middle
# so each time it checks an item, it eliminates half the remaining items from consideration
def iterativeBinarySearch(alist, item):
    first = 0  # keep track of the current "bounds" of the part of the list we are paying attention to
    last = len(alist) - 1  # the bounds start at the ends of the list
    found = False  # so we can stop if we have found the list

    # end the loop if we are done or if the relevant part of the list is of zero length or less
    while first <= last and not found:
        midpoint = (first + last) // 2  # choose as close to the midpoint of the list as we can
        if alist[midpoint] == item:
            found = True  # if we have a match at the chosen index, we are done
        else:
            if item < alist[midpoint]:  # if the target item is less than that at the chosen index, search the left half
                last = midpoint - 1  # constrict the "last" index to right before the midpoint
            else:  # if not, the item is on the right half of the list by elimination
                first = midpoint + 1  # constrict the "first" index to right after the midpoint

    return found  # if we get to a zero length list without finding the item, it is not there


# same theoretical method, just different implementation
def recursiveBinarySearch(alist, item):
    if len(alist) == 0:  # base case: an empty list obviously does not contain the item
        return False
    else:
        midpoint = len(alist) // 2  # want to check the middle of the list (or as close as we can get)
        if alist[midpoint] == item:  # we have found the item --> we are done
            return True
        else:
            # recurse on either half of the list
            if item < alist[midpoint]:  # if the item is smaller than the midpoint, it is in the left half
                return recursiveBinarySearch(alist[:midpoint], item)
            else:  # if greater, the item is on the right
                return recursiveBinarySearch(alist[midpoint + 1:], item)


# test: run for increasing sizes of lists; use timeit.Timer for more accuracy/reproducibility
for i in range(10000, 100001, 10000):
    # create two timers that each run one of the functions
    t1 = Timer("iterativeBinarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,iterativeBinarySearch,list1")
    list1 = sorted([random.randrange(i) for k in range(i)])  # randomly generated a list, then sort it

    t2 = Timer("recursiveBinarySearch(list1, random.randrange(%d))" % i,
               "from __main__ import random,recursiveBinarySearch,list1")

    # uncomment these two lines to output length and time as points in the coordinate plane for graphing
    # print("(" + str(i / 10000) + ", " + str(t1.timeit(1000)) + ")")  # (x, y) format for graphing, iterative
    # print("(" + str(i / 10000) + ", " + str(t2.timeit(1000)) + ")")  # (x, y) format for graphing, recursive
    print("Iterative -> Length: " + str(i) + "; Time: " + str(t1.timeit(1000)))  # verbose output,   iterative
    print("Recursive -> Length: " + str(i) + "; Time: " + str(t2.timeit(1000)))  # verbose output,   recursive
