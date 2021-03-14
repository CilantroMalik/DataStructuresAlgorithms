import random
from timeit import Timer
from os import system

"""
--- Selection Sort with Simultaneous Assignment ---
Implementation of selection sort that takes advantage of Python's simultaneous assignment feature for swapping the
values of two variables to slightly optimize the selection sort algorithm's use of swaps during the course of its execution.
At the end, a timed test is included to pit the two versions against each other to measure the effect of the change.
"""

# standard selection sort implementation: on each pass, finds the largest item in the list and places it in its proper position
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):  # keep track of which index we have to fill on this pass
        positionOfMax = 0  # where is the largest item?
        for location in range(1, fillslot + 1):  # only loop through items up until the slot we have to fill
            if alist[location] > alist[positionOfMax]:  # if we have a new max, set the variable to keep track of that
                positionOfMax = location

        temp = alist[fillslot]  # swap the largest item (at the position that we kept track of) with the item in the fill slot
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


# alternate implementation that uses simultaneous assignment for a slightly more efficient swap
def selectionSortSimul(alist):
    for fillslot in range(len(alist) - 1, 0, -1):  # all of this logic is the same
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        # the only different step is the swap: 1 line instead of three, because we use simultaneous assignment and no temporary variable
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


# Performance Analysis

nonSimul, simul = 0, 0  # keep track of the total times

for i in range(500):  # test on 500 random lists
    list1 = random.sample(range(1000), 500)  # each list is 500 numbers long
    t1 = Timer("selectionSort(list1)", "from __main__ import selectionSort,list1")
    t2 = Timer("selectionSortSimul(list1)", "from __main__ import selectionSortSimul,list1")

    nonSimul += t1.timeit(10)  # time each one 10 times to eliminate inconsistencies
    simul += t2.timeit(10)

    # provide feedback on the program's progress since it will take a while
    if i % 5 == 0:  # only increment a percent every 10 iterations since we are going 1000 times
        system('clear')  # helps create a more seamless loading effect
        print(f"Loading: {i // 5 + 1}%")  # show how far we are through the script, since it takes a while
        print("|" + ("=" * (i // 10 + 1)).ljust(50) + "|")  # "progress bar" effect

print("Without Simultaneous Assignment: " + str(nonSimul))
print("With Simultaneous Assignment:    " + str(simul))

# *** RESULT: No simultaneous assignment (barely) wins! ***
