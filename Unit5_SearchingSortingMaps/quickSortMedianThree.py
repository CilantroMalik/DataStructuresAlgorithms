import random
from timeit import Timer


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


def quickSortMedianThree(alist):
    quickSortHelperMedianThree(alist, 0, len(alist) - 1)


def quickSortHelperMedianThree(alist, first, last):
    if first < last:
        splitpoint = partitionMedianThree(alist, first, last)

        quickSortHelperMedianThree(alist, first, splitpoint - 1)
        quickSortHelperMedianThree(alist, splitpoint + 1, last)


def partitionMedianThree(alist, first, last):
    mid = first + (length(first, last) // 2)
    pivotvalue = sorted([alist[first], alist[last], alist[mid]])[1]

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


def length(start_index, end_index):
    return end_index - start_index + 1


total = 0
for i in range(100):
    list1 = random.sample(range(1000), 500)
    control = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    total += control.timeit(25)
print(f"Normal quicksort: {total/100}")

total = 0
for i in range(100):
    list1 = random.sample(range(1000), 500)
    sorter = Timer(f"quickSortMedianThree(list1)",
                   "from __main__ import quickSortMedianThree,list1")
    total += sorter.timeit(25)
print(f"Median of Three: {total/100}")
