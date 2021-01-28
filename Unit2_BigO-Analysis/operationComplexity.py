import time
from random import randrange


# test 1: list get operator. implemented as O(1), and results should reflect this
def listIndex(alist, i):
    return alist[i]


# test 2: dictionary get operator. implemented as O(1)
def dictIndex(adict, i):
    return adict[i]


# test the operations for time complexity
# TODO switch timing to timeit.Timer for higher accuracy and repeatability
for listSize in range(1000, 10001, 1000):
    print("list size:", listSize, end=' || ')  # prepare for the later outputs

    # create data structures for testing, made of random numbers from 1 to 10000
    numList = [randrange(0, 10000) for i in range(listSize)]
    numDict = {i: randrange(0, 10000) for i in range(listSize)}
    # determine the index separately instead of inline so the randrange() call doesn't interfere with timing
    rand_index = randrange(0, listSize - 1)
    # test list get operator and print results
    start = time.time()
    listIndex(numList, rand_index)
    end = time.time()
    print(f"list get: {round(end - start, 12)}s | ", end='')
    # test dict get operator and print results
    start = time.time()
    listIndex(numDict, rand_index)
    end = time.time()
    print(f"dict get: {round(end - start, 12)}s")
