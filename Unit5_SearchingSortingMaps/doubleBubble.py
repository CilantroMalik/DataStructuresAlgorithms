import random
from timeit import Timer
from os import system

"""
--- Bi-Directional Bubble Sort ---
Implementation of the conventional bubble sort algorithm that instead moves both forward and backward, instead of just
one direction, in an alternating fashion. It will "bubble up" going from the start to the end of the list and swapping
as per its normal behavior, then on the next pass it will "bubble down" and swap according to the lowest element with
the goal of getting that to the bottom. This way it fills the list from both ends inward instead of only one end.
"""

# this algorithm has already been thoroughly commented on another exercise
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


# alternate implementation of bubble sort that works both ways alternating
def doubleBubble(alist):
    upPasses = 0  # keep track of the total passes in each direction so we know where to start
    downPasses = 0
    for passnum in range(len(alist)):
        if passnum % 2 == 0:  # first, third, fifth, etc passes -> bubble up
            for i in range(len(alist)-upPasses-1):  # want to get the highest number to the end of the list
                if alist[i] > alist[i + 1]:  # so we compare if a number is greater than the next and if so, swap it
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            upPasses += 1
        else:  # second, fourth, sixth, etc passes -> bubble down
            for j in range(len(alist)-downPasses-1, 0, -1):  # want to get the lowest number to the beginning of the list
                if alist[j] < alist[j - 1]:  # so we compare if a number is less than the next and if so, swap it
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]
            downPasses += 1


# Performance Analysis

single, double = 0, 0  # keep track of total times

for i in range(500):  # test on 500 random lists
    list1 = random.sample(range(1000), 500)  # each list is 500 numbers long
    t1 = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    t2 = Timer("doubleBubble(list1)", "from __main__ import doubleBubble,list1")

    single += t1.timeit(10)  # time each one 10 times to eliminate inconsistencies
    double += t2.timeit(10)

    # provide feedback on the program's progress since it will take a while
    if i % 5 == 0:  # only increment a percent every 10 iterations since we are going 1000 times
        system('clear')  # helps create a more seamless loading effect
        print(f"Loading: {i // 5 + 1}%")  # show how far we are through the script, since it takes a while
        print("|" + ("=" * (i // 10 + 1)).ljust(50) + "|")  # "progress bar" effect

print("Normal Bubble Sort: " + str(single))  # report the results
print("Double Bubble Sort: " + str(double))

# RESULT: Normal bubble sort wins!
