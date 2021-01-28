import time
from random import randrange


# test 1: list get operator. implemented as O(1), and results should reflect this
def listIndex(alist, i):
    return alist[i]


# test the operations for time complexity
for listSize in range(1000, 10001, 1000):
    nums = [randrange(0, 10000) for i in range(listSize)]  # list of random values from 0 to 10000
    # determine the index separately instead of inline so the randrange() call doesn't interfere with timing
    rand_index = randrange(0, listSize - 1)
    start = time.time()
    returned = listIndex(nums, rand_index)
    end = time.time()
    # print summary of results
    print(f"size: {listSize} returned: {returned} time: {end - start}")
