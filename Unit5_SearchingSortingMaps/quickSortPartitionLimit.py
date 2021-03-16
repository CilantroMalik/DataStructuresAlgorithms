import random
from timeit import Timer

"""
--- Quick Sort with Partition Limit ---
Implementation of the Quick Sort algorithm that experiments with a partition limit, which is a lower bound on the length
of a sub-list such that if a list is shorter than the partition limit, it is passed directly into insertion sort rather
than having to go through the quick sort process. The idea behind it is that quick sort has recursive calls and therefore
significant overhead for small lists since log n grows quickly for small numbers, so if the smaller lists are insertion
sorted directly it removes a significant number of the recursive calls (there will always be more at the bottom of the tree
than at the top, orders of magnitude more in fact). This program implements this measure, then tests a variety of partition
limits against the "traditional" implementation and against each other to see which ones are the most efficient.
"""

# normal insertion sort algorithm, except takes start and end parameters because it is only sorting a sublist
def insertionSort(alist, start, end):
    for index in range(start + 1, end + 1):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


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


# partition limit implementation of quicksort
def quickSortPartition(alist, partitionLimit):
    def _quickSortPartition(alist, leftmark, rightmark, partitionLimit):
        if leftmark < rightmark:  # similar logic to normal quicksort
            if (rightmark - leftmark + 1) >= partitionLimit:  # but we have this extra check: is the list longer than the limit?
                splitpoint = partition(alist, leftmark, rightmark)  # partition as normal and run recursive calls as usual

                _quickSortPartition(alist, leftmark, splitpoint-1, partitionLimit)
                _quickSortPartition(alist, splitpoint+1, rightmark, partitionLimit)
            else:  # if it is shorter than the limit, simply insertion sort this sublist
                insertionSort(alist, leftmark, rightmark)

    _quickSortPartition(alist, 0, len(alist)-1, partitionLimit)  # run our helper function with the appropriate parameters


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


# -- Performance Analysis --
print("-- Average Times --")
print("———————————————————")
total = 0  # keep track of the total time
for i in range(100):  # 100 trials so the algorithm gets to work on 100 different lists
    list1 = random.sample(range(5000), 1000)  # each list is length 1000 and made of random numbers from 1 to 5000
    control = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    total += control.timeit(25)  # time each one 25 times for consistency
print(f"Normal quicksort:     {total/100}")  # give the average time

for partitionLimit in range(2, 100):  # test on partition limits from 2 (obviously the minimum) up to 100
    total = 0  # for each partition limit run a nearly identical procedure to above: 100 lists, each 1000 numbers, timed 25x each
    for i in range(100):
        list1 = random.sample(range(5000), 1000)
        sorter = Timer(f"quickSortPartition(list1, {partitionLimit})",
                       "from __main__ import quickSortPartition,list1")
        total += sorter.timeit(25)

    print(f"Partition limit of {partitionLimit}: {total/100}")
