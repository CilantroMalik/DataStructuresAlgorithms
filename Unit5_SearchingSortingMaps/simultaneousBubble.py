import random
from timeit import Timer
from os import system

"""
--- Bubble Sort with Simultaneous Assignment ---
Implementation of the bubble sort algorithm taking advantage of Python's simultaneous assignment functionality
since bubble sort utilizes large amount of swaps, and simultaneous assignment internally makes each swap slightly more
efficient. The "traditional" implementation and this one are then compared in a timed test to quantify the improvement.
"""

# normal bubble sort implementation
def bubbleSort(alist):
    # run as many passes as items in the list; start with the entire list and narrow down
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):  # for each element up to the current "focus" (which is encoded by passnum)
            if alist[i] > alist[i + 1]:  # is this element greater than the next? if so, swap them
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# improved implementation: same logic, except the swap step is now a single line
def bubbleSortSimul(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:  # swap using simultaneous assignment instead of a temporary variable
                alist[i], alist[i+1] = alist[i+1], alist[i]


# Performance Analysis

nonSimul, simul = 0, 0  # store the total times

for i in range(1000):  # run on 1000 different lists to eliminate errors
    list1 = random.sample(range(1000), 500)  # lists of size 500 made of random numbers from 1 to 1000
    t1 = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    t2 = Timer("bubbleSortSimul(list1)", "from __main__ import bubbleSortSimul,list1")

    # time each one 10 times to eliminate small inaccuracies
    nonSimul += t1.timeit(10)
    simul += t2.timeit(10)

    # display a little feedback to the user because this takes quite a while to run
    if i % 10 == 0:  # only increment a percent every 10 iterations since we are going 1000 times
        system('clear')  # helps create a more seamless loading effect
        print(f"Loading: {i // 10 + 1}%")  # show how far we are through the script, since it takes a while
        print("|" + ("=" * (i // 20 + 1)).ljust(50) + "|")  # "progress bar" effect

print("Without Simultaneous Assignment: " + str(nonSimul))
print("With Simultaneous Assignment:    " + str(simul))

# *** RESULT: Simultaneous assignment wins! ***
