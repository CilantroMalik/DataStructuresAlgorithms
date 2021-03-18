import random
from timeit import Timer

"""
--- Quick Sort with Median-of-Three Pivot Value Selection ---
Alternate version of quick sort that implements median-of-three as a technique for selecting the pivot value during
partitioning. This technique looks at the first, last, and middle value and selects the median of them, aiming to choose
the pivot that most evenly splits the list in two while not adding too much extra time complexity to the process.
Additionally, this module includes a timed experiment to test the algorithms with and without this modification.
"""

# "traditional" quicksort implementation
def quickSort(alist):
    def _quickSort(alist, leftmark, rightmark):  # define an inner helper function that takes in the extra parameters
        if leftmark < rightmark:  # base case: if the sublist is of length 1 or less, it is by definition sorted; only continue if this is not true
            splitpoint = partition(alist, leftmark, rightmark)  # partition the list with a helper function
            _quickSort(alist, leftmark,
                       splitpoint - 1)  # then recursively quicksort the two sublists determined by the split point
            _quickSort(alist, splitpoint + 1, rightmark)

    _quickSort(alist, 0,
               len(alist) - 1)  # call our helper function with the first and last indices as initial parameters


# partitioning function; will be common between the two implementations
def partition(alist, leftmark, rightmark):
    pos = leftmark - 1  # start the position at one below the left index
    pivot = alist[leftmark + (rightmark - leftmark) // 2]  # choose pivot value in the middle
    for j in range(leftmark, rightmark):  # for every element in the sublist
        if alist[j] <= pivot:  # if less than pivot, swap it on the left of the pivot; those greater than the pivot end up on the right
            pos = pos + 1  # increment the swap position, then swap the current element and the one at this position
            alist[pos], alist[j] = alist[j], alist[pos]  # use simultaneous assignment for slightly more efficiency and no temp variable
    alist[pos + 1], alist[rightmark] = alist[rightmark], alist[pos + 1]  # make the final swap
    return pos + 1  # return the split point


# alternate implementation: exactly identical logic in this function, the only difference is in the partitioning function
def quickSortM3(alist):
    def _quickSortM3(alist, leftmark, rightmark):
        if leftmark < rightmark:
            splitpoint = partitionM3(alist, leftmark, rightmark)

            _quickSortM3(alist, leftmark, splitpoint - 1)
            _quickSortM3(alist, splitpoint + 1, rightmark)
    _quickSortM3(alist, 0, len(alist) - 1)

def partitionM3(alist, leftmark, rightmark):
    mid = leftmark + (length(leftmark, rightmark) // 2)
    # this is the unique element of this algorithm: choose the median element between the first, last, and middle elements
    # one approach is to simply sort the 3 item-list, which will essentially happen in negligible time, then take the middle element
    pivot = sorted([alist[leftmark], alist[rightmark], alist[mid]])[1]

    # alternate way of doing the same thing without sorting: check which element is in between the others (median)
    # if alist[leftmark] <= alist[mid] <= alist[rightmark] or alist[rightmark] <= alist[mid] <= alist[leftmark]:
    #     pivot = alist[mid]
    # elif alist[mid] <= alist[leftmark] <= alist[rightmark] or alist[rightmark] <= alist[leftmark] <= alist[mid]:
    #     pivot = alist[leftmark]
    # else:
    #     pivot = alist[rightmark]

    pos = leftmark - 1  # start the position at one below the left index
    for j in range(leftmark, rightmark):  # for every element in the sublist
        if alist[j] <= pivot:  # if less than pivot, swap it on the left of the pivot; those greater than the pivot end up on the right
            pos = pos + 1  # increment the swap position, then swap the current element and the one at this position
            alist[pos], alist[j] = alist[j], alist[pos]  # use simultaneous assignment for slightly more efficiency and no temp variable
    alist[pos + 1], alist[rightmark] = alist[rightmark], alist[pos + 1]  # make the final swap
    return pos + 1  # return the split point


# light helper function that simply calculates the length of a list given start and end indices; mostly for convenience and readability
def length(start_index, end_index):
    return end_index - start_index + 1


# -- Performance Analysis --

total = 0  # stores the total time
for i in range(100):  # same process as always: 100 times through for 100 different test lists
    list1 = random.sample(range(1000), 500)  # each list is 500 numbers long
    control = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    total += control.timeit(25)  # and we time 25 times to mitigate small number inconsistencies
print(f"Normal quicksort: {total/100}")  # then output the average time

total = 0  # same exact approach for timing of the alternate implementation
for i in range(100):
    list1 = random.sample(range(1000), 500)
    sorter = Timer(f"quickSortM3(list1)", "from __main__ import quickSortM3,list1")
    total += sorter.timeit(25)
print(f"Median of Three: {total/100}")

# *** RESULTS: normal quicksort wins! ***
