import time
from timeit import Timer
from random import randrange


# test 1: list get operator. implemented as O(1)
def listGet(alist, i):
    return alist[i]


# test 2: dictionary get operator. implemented as O(1)
def dictGet(adict, i):
    return adict[i]


# test 3: dictionary set operator. implemented as O(1)
def dictSet(adict, i):
    adict[i] = 1234
    return adict


# test the operations on increasingly large lists to see their time complexity
for listSize in range(1000, 10001, 1000):
    print("list size:", listSize, end=' || ')  # prepare for the later outputs

    # create data structures for testing, made of random numbers from 1 to 10000
    numList = [randrange(0, 10000) for i in range(listSize)]
    numDict = {i: randrange(0, 10000) for i in range(listSize)}
    # determine the index separately instead of inline so the randrange() call doesn't interfere with timing
    randIndex = randrange(0, listSize - 1)

    # create the timers that will run each of the tests
    timer1 = Timer("listGet(numList, randIndex)", "from __main__ import listGet, numList, randIndex")
    timer2 = Timer("dictGet(numDict, randIndex)", "from __main__ import dictGet, numDict, randIndex")
    timer3 = Timer("dictSet(numDict, randIndex)", "from __main__ import dictSet, numDict, randIndex")

    # test the three operations, each 10000 times to make up for the fact that they are so short
    print(f"list get: {round(timer1.timeit(10000), 12)}s | ", end='')
    print(f"dict get: {round(timer2.timeit(10000), 12)}s | ", end='')
    print(f"dict set: {round(timer3.timeit(10000), 12)}s")
