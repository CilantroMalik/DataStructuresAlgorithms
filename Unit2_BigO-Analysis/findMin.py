import time
from random import randrange

# TODO add docstring and more comments in the code


# find minimum item in a list in O(n^2)
def inefficientFindMin(alist):
    current_min = alist[0]
    for num in alist:
        is_min = True
        for other in alist:
            if other < num:
                is_min = False
        if is_min:
            current_min = num
    return current_min


# find minimum item in a list in O(n)
def findMin(alist):
    # TODO minor optimization to skip 1st element?
    current_min = alist[0]
    for num in alist:
        if num < current_min:
            current_min = num
    return current_min


# time comparison between the two approaches on relatively large lists
# TODO use timeit.Timer approach for more accurate measurement of runtime
for listSize in range(1000, 10001, 1000):
    nums = [randrange(0, 10000) for i in range(listSize)]
    start = time.time()
    inefficientFindMin(nums)
    end = time.time()
    print(f"size: {listSize}, time for O(n^2): {end - start}")
    start = time.time()
    findMin(nums)
    end = time.time()
    print(f"size: {listSize}, time for O(n):   {end - start}")
