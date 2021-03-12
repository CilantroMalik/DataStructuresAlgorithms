import random


# normal merge sort implementation: uses slice operator
def mergeSortSlice(alist):
    if len(alist) > 1:  # base case: list has to be larger than one because a one element list is sorted by definition
        mid = len(alist) // 2  # integer midpoint index of the list
        lefthalf = alist[:mid]  # split the list into two sublists based on that midpoint
        righthalf = alist[mid:]

        # and recursively sort each half
        mergeSortSlice(lefthalf)
        mergeSortSlice(righthalf)

        # now to merge them. first create three index variables
        i = 0  # keeps track of current position in the left half
        j = 0  # keeps track of current position in the right half
        k = 0  # keeps track of current position in the final list
        while i < len(lefthalf) and j < len(righthalf):  # while the positions have not reached the end of their respective lists
            if lefthalf[i] <= righthalf[j]:  # if the left half is less or if they are equal, put the one in the left first
                alist[k] = lefthalf[i]
                i = i + 1  # and increment the corresponding index
            else:  # if the right half was smaller, put that first
                alist[k] = righthalf[j]
                j = j + 1  # and increment the corresponding index
            k = k + 1  # either way, we added one item to the final list, so increment this index

        while i < len(lefthalf):  # add all the remaining elements from the left half
            alist[k] = lefthalf[i]
            i = i + 1  # incrementing relevant indices each time
            k = k + 1

        while j < len(righthalf):  # then add all the remaining elements from the right half
            alist[k] = righthalf[j]
            j = j + 1  # increment the applicable indices
            k = k + 1


# implementation that does not use the slice operator
def mergeSort(alist):  # wrapper function for the helper that has to take in extra parameters
    mergeSortHelper(alist, 0, len(alist)-1)


def mergeSortHelper(alist, start, end):
    if length(start, end) > 1:  # same base case, just have to calculate the length using indices
        mid = start + (length(start, end) // 2)  # same midpoint calculation, but we have to take into account the indices

        mergeSortHelper(alist, start, mid-1)  # again, recursively sort both halves, but this time just modify the indices
        mergeSortHelper(alist, mid, end)

        merge(alist, start, mid, end)  # we have offloaded the merging procedure into a helper function


def merge(alist, start1, start2, end2):  # take in the start and end of each sublist (start of second = end of first)
    i = start1
    j = start2
    while i <= start2 and j <= end2:  # same logic, just slightly different conditions
        if alist[i] < alist[j]:  # if the left half item is less, just add one to the index, we will return to it later
            i += 1
        else:
            temp = alist[j]  # store the item at the current position, we will be moving it
            for index in range(j-1, i-1, -1):  # shift all items down one position until the current left index
                alist[index+1] = alist[index]
            alist[i] = temp  # then replace the current position with the item we wanted
            i += 1  # increment the relevant indices
            j += 1
            start2 += 1  # increment the "start" of the right list because the left list has had one element added to it


def length(start_index, end_index):  # helper function that calculates the length of a list given start and end indices
    return end_index - start_index + 1  # short but reduces clutter and improves readability of the main logic
