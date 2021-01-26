import time
from random import randrange


# Test Function
def findMin(alist):
    current_min = 9999999999
    for num in alist:
        if num < current_min:
            current_min = num
    return current_min


# Test Loop
for listSize in range(1000, 10001, 1000):
    nums = [randrange(0, 10000) for i in range(listSize)]
    start = time.time()
    findMin(nums)
    end = time.time()
    print(f"size: {listSize} time: {end - start}")
