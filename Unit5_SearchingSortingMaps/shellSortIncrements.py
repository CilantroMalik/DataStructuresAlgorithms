import math
import random
from timeit import Timer
from os import system

"""
--- Shell Sort Increment Experimentation ---
Provides two implementations of the Shell Sort algorithm with different schemes for how to divide the list into
sublists for sorting by this algorithm. One of them uses simple division by 2 to come up with the increments, while
the other uses Mersenne numbers for increments, as these have been mathematically determined to be among the most
efficient incrementing schemes for this family of algorithm. Otherwise, the logic is identical — each sublist is sorted
with a slightly modified insertion sort, then the increments are re-computed and the process starts again, and by the end 
the whole list is sorted. We also include a timed test at the end to compare the two implementations.
"""

# shell sort implementation
def shellSort(alist):
    sublistcount = len(alist) // 2  # how many sublists?
    while sublistcount > 0:
        # for each sublist, call a helper function with that as the start position and the required increment
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2  # halve the count for the next iteration of the loop


# modified implementation: use Mersenne numbers, those of the form 2^n - 1, as increments for optimal efficiency
def shellSortNewIncrements(alist):
    # finding the greatest Mersenne number less than len(alist)
    sublistcount = int(math.pow(2, int(math.log(len(alist), 2)))) - 1
    while sublistcount > 0:
        # same logic here as before
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        # making the next lower Mersenne number: add 1 -> perfect power of 2, then divide by 2 and subtract one to
        # make it a Mersenne number again [started with 2^k - 1 --> ending with 2^(k-1) - 1]
        sublistcount = (sublistcount + 1) // 2 - 1


def gapInsertionSort(alist, start, gap):  # insertion sort, but taking the gap into account
    for i in range(start + gap, len(alist), gap):  # range object that skips numbers with the given interval

        currentvalue = alist[i]
        position = i
        # sort as normal, scanning through the list and updating the position value as we go
        while position >= gap and alist[position - gap] > currentvalue:  # have to decrement by 'gap' instead of 1
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue  # same as normal insertion sort


# Performance Analysis

original, new = 0, 0  # keep track of the total times

for i in range(500):  # test on 500 random lists
    list1 = random.sample(range(1000), 1000)  # each list is 1000 numbers long
    t1 = Timer("shellSort(list1)", "from __main__ import shellSort,list1")
    t2 = Timer("shellSortNewIncrements(list1)", "from __main__ import shellSortNewIncrements,list1")

    original += t1.timeit(10)  # time each one 10 times to minimize inconsistencies
    new += t2.timeit(10)

    # provide feedback on the program's progress since it will take a while
    if i % 5 == 0:  # only increment a percent every 10 iterations since we are going 1000 times
        system('clear')  # helps create a more seamless loading effect
        print(f"Loading: {i // 5 + 1}%")  # show how far we are through the script, since it takes a while
        print("|" + ("=" * (i // 10 + 1)).ljust(50) + "|")  # "progress bar" effect

print("Original Increments: " + str(original))
print("New Increments:      " + str(new))

# *** RESULT: New increment scheme (Mersenne numbers) wins! ***
