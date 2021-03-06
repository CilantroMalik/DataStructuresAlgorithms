from timeit import Timer
import random
from os import system


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

def quickSort(input_list):
    def _quickSort(input_list, leftmark, rightmark):
        if leftmark < rightmark:
            splitpoint = partition(input_list, leftmark, rightmark)
            _quickSort(input_list, leftmark, splitpoint - 1)
            _quickSort(input_list, splitpoint + 1, rightmark)
    _quickSort(input_list, 0, len(input_list)-1)


def partition(input_list, leftmark, rightmark):
    pos = leftmark - 1
    pivot = input_list[leftmark + (rightmark - leftmark) // 2]
    for j in range(leftmark, rightmark):
        if input_list[j] <= pivot:
            pos = pos + 1
            input_list[pos], input_list[j] = input_list[j], input_list[pos]
    input_list[pos+1], input_list[rightmark] = input_list[rightmark], input_list[pos + 1]
    return pos + 1

# --------------------- ANALYSIS ---------------------


bubbleTotal, selectionTotal, insertionTotal, shellTotal, mergeTotal, quickTotal, timTotal = 0, 0, 0, 0, 0, 0, 0

for i in range(100):
    # READY...
    list1 = random.sample(range(5000), 2000)

    # SET...
    bubble = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    selection = Timer("selectionSort(list1)", "from __main__ import selectionSort,list1")
    insertion = Timer("insertionSort(list1)", "from __main__ import insertionSort,list1")
    shell = Timer("shellSort(list1)", "from __main__ import shellSort,list1")
    merge = Timer("mergeSort(list1)", "from __main__ import mergeSort,list1")
    quick = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    timsort = Timer("list1.sort()", "from __main__ import list1")
    # FIGHT!
    bubbleTotal += bubble.timeit(10)
    selectionTotal += selection.timeit(10)
    insertionTotal += insertion.timeit(10)
    shellTotal += shell.timeit(10)
    mergeTotal += merge.timeit(10)
    quickTotal += quick.timeit(10)
    timTotal += timsort.timeit(10)

    system('clear')
    print(f"Loading: {i+1}%")
    print("|" + ("="*(i//2 + 1)).ljust(50) + "|")

print("Bubble Sort Total:", bubbleTotal)
print("Selection Sort Total:", selectionTotal)
print("Insertion Sort Total:", insertionTotal)
print("Shell Sort Total:", shellTotal)
print("Merge Sort Total:", mergeTotal)
print("Quick Sort Total:", quickTotal)
print("Native Sort Total:", timTotal)
