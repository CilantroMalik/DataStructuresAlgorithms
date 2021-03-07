from timeit import Timer
import random
from os import system


"""
--- Sorting Algorithm Benchmark ---
Program that implements a variety of sorting algorithms, and then pits them against each other in a timed test
on randomly generated lists in order to see which are the fastest. The test runs multiple trials on each list 
as well as testing on multiple lists in order to minimize variance in many different ways.
"""


# =======================================================
# =================Algorithm Definitions=================
# =======================================================

# --------------------- BUBBLE SORT ---------------------


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


# --------------------- SELECTION SORT ---------------------


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


# --------------------- INSERTION SORT ---------------------


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue


# --------------------- SHELL SORT ---------------------


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


# --------------------- MERGE SORT ---------------------


def mergeSort(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    # print("Merging ", alist)


# --------------------- QUICK SORT ---------------------

def quickSort(alist):
    def _quickSort(alist, leftmark, rightmark):
        if leftmark < rightmark:
            splitpoint = partition(alist, leftmark, rightmark)
            _quickSort(alist, leftmark, splitpoint - 1)
            _quickSort(alist, splitpoint + 1, rightmark)
    _quickSort(alist, 0, len(alist) - 1)


def partition(alist, leftmark, rightmark):
    pos = leftmark - 1
    pivot = alist[leftmark + (rightmark - leftmark) // 2]
    for j in range(leftmark, rightmark):
        if alist[j] <= pivot:
            pos = pos + 1
            alist[pos], alist[j] = alist[j], alist[pos]
    alist[pos + 1], alist[rightmark] = alist[rightmark], alist[pos + 1]
    return pos + 1

# --------------------- ANALYSIS ---------------------


# create variables to store total times for each sorting algorithm
bubbleTotal, selectionTotal, insertionTotal, shellTotal, mergeTotal, quickTotal, timTotal = 0, 0, 0, 0, 0, 0, 0

for i in range(100):  # run 100 trials, so the algorithms get tested on different lists
    # READY...
    list1 = random.sample(range(5000), 2000)  # test list of size 2000, numbers from 1 to 5000

    # SET...
    bubble = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")  # create timers for each sorting algorithm
    selection = Timer("selectionSort(list1)", "from __main__ import selectionSort,list1")
    insertion = Timer("insertionSort(list1)", "from __main__ import insertionSort,list1")
    shell = Timer("shellSort(list1)", "from __main__ import shellSort,list1")
    merge = Timer("mergeSort(list1)", "from __main__ import mergeSort,list1")
    quick = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    timsort = Timer("list1.sort()", "from __main__ import list1")
    # FIGHT!
    bubbleTotal += bubble.timeit(10)  # then time them, 10 times to remove some small-number random error
    selectionTotal += selection.timeit(10)
    insertionTotal += insertion.timeit(10)
    shellTotal += shell.timeit(10)
    mergeTotal += merge.timeit(10)
    quickTotal += quick.timeit(10)
    timTotal += timsort.timeit(10)

    system('clear')  # create the loading screen effect
    print(f"Loading: {i+1}%")  # show how far we are through the script, since it takes a while
    print("|" + ("="*(i//2 + 1)).ljust(50) + "|")  # "progress bar" effect

# finally, print out the totals so we can compare
print("Bubble Sort Total:", bubbleTotal)
print("Selection Sort Total:", selectionTotal)
print("Insertion Sort Total:", insertionTotal)
print("Shell Sort Total:", shellTotal)
print("Merge Sort Total:", mergeTotal)
print("Quick Sort Total:", quickTotal)
print("Native Sort Total:", timTotal)
