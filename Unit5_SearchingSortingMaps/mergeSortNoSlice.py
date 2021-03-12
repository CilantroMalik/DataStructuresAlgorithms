import random


def mergeSortSlice(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortSlice(lefthalf)
        mergeSortSlice(righthalf)

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


def mergeSort(alist):
    mergeSortHelper(alist, 0, len(alist)-1)


def mergeSortHelper(alist, start, end):
    if length(start, end) > 1:
        mid = start + (length(start, end) // 2)

        mergeSortHelper(alist, start, mid-1)
        mergeSortHelper(alist, mid, end)

        merge(alist, start, mid, end)


def merge(alist, start1, start2, end2):
    i = start1
    j = start2
    while i <= start2 and j <= end2:
        if alist[i] < alist[j]:
            i += 1
        else:
            temp = alist[j]
            for index in range(j-1, i-1, -1):
                alist[index+1] = alist[index]
            alist[i] = temp
            i += 1
            j += 1
            start2 += 1


def length(start_index, end_index):
    return end_index - start_index + 1
