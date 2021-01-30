"""
--- findK implementation in O(n log n) ---
Implementation of the function findK, which finds the k-th smallest number in a list, in O(n log n) time.
Utilizes merge sort, which has the same time complexity, to do most of the heavy lifting.
"""

# parameters: the list to be processed, and the k-value that determines which smallest element to find
def findK(alist, k):
    # sort the list in ascending order, so the smallest number is first, second smallest is second, etc
    # as alluded to above, merge sort works in O(n log n) time
    mergeSort(alist)
    # then return the b-th smallest number (subtracting one to account for list indices counting from zero)
    return alist[k - 1]


# helper function: sort the list using a standard implementation of the merge sort algorithm
def mergeSort(alist):
    # base case occurs if the list is only one element, in which case it is sorted
    if len(alist) > 1:
        # split the list into two halves using slicing, then recursively sort each half
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # now merge the halves together.
        # make variables to keep track of how far we are through each half and where we are in the merged list
        i = 0
        j = 0
        k = 0
        # compare the items at the indices; whichever is less, put it in the final list,
        # then increment the relevant indices by 1 to keep their place
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # if items are left over in either list, add them
        # to the end of the merged list in order
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
