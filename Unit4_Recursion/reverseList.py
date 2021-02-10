"""
--- Recursive List Reversal ---
Simple function that reverses a list by recursively creating the reverse through extracting the last element and
using tail recursion to slowly whittle down the list and build up the output in the call stack.
"""


def reverse(alist):
    if len(alist) == 1:  # base case: one-item list is its own reverse
        return alist
    else:  # recursive case: last element plus the reverse of everything else
        return [alist[-1]] + reverse(alist[:-1])  # need to wrap the individual item in a list so concatenation works
