from timeit import Timer
import random


# =======================================================
# =================Algorithm Definitions=================
# =======================================================

# --------------------- BUBBLE SORT ---------------------


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# --------------------- SELECTION SORT ---------------------


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


# --------------------- INSERTION SORT ---------------------


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

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
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# --------------------- ANALYSIS ---------------------

bubbleTotal, selectionTotal, insertionTotal, shellTotal, mergeTotal, quickTotal = 0, 0, 0, 0, 0, 0

for i in range(100):
    # READY...
    list1 = random.sample(range(5000), 500)

    # SET...
    bubble = Timer("bubbleSort(list1)", "from __main__ import bubbleSort,list1")
    selection = Timer("selectionSort(list1)", "from __main__ import selectionSort,list1")
    insertion = Timer("insertionSort(list1)", "from __main__ import insertionSort,list1")
    shell = Timer("shellSort(list1)", "from __main__ import shellSort,list1")
    merge = Timer("mergeSort(list1)", "from __main__ import mergeSort,list1")
    quick = Timer("quickSort(list1)", "from __main__ import quickSort,list1")

    # FIGHT!
    bubbleTotal += bubble.timeit(10)
    selectionTotal += selection.timeit(10)
    insertionTotal += insertion.timeit(10)
    shellTotal += shell.timeit(10)
    mergeTotal += merge.timeit(10)
    quickTotal += quick.timeit(10)

    print(f"Loading: {i+1}%")

print("Bubble Sort Total: " + str(bubbleTotal))
print("Selection Sort Total: " + str(selectionTotal))
print("Insertion Sort Total: " + str(insertionTotal))
print("Shell Sort Total: " + str(shellTotal))
print("Merge Sort Total: " + str(mergeTotal))
print("Quick Sort Total: " + str(quickTotal))
