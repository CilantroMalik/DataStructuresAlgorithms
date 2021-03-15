import random
from timeit import Timer


def insertionSort(alist, start, end):
    for index in range(start + 1, end + 1):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


def quickSortPartition(alist, partitionLimit):
    quickSortHelperPartition(alist, 0, len(alist) - 1, partitionLimit)


def quickSortHelperPartition(alist, first, last, partitionLimit):
    if first < last:
        if (last - first + 1) >= partitionLimit:
            splitpoint = partition(alist, first, last)

            quickSortHelperPartition(alist, first, splitpoint - 1, partitionLimit)
            quickSortHelperPartition(alist, splitpoint + 1, last, partitionLimit)
        else:
            insertionSort(alist, first, last)


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


# test = random.sample(range(5000), 1000)
# quickSortPartition(test, 3)
# print(test)

total = 0
for i in range(100):
    list1 = random.sample(range(5000), 1000)
    control = Timer("quickSort(list1)", "from __main__ import quickSort,list1")
    total += control.timeit(25)
print(f"Normal quicksort:     {total/100}")

for partitionLimit in range(2, 25):
    total = 0
    for i in range(100):
        list1 = random.sample(range(5000), 1000)
        sorter = Timer(f"quickSortPartition(list1, {partitionLimit})",
                       "from __main__ import quickSortPartition,list1")
        total += sorter.timeit(25)

    print(f"Partition limit of {partitionLimit}: {total/100}")
