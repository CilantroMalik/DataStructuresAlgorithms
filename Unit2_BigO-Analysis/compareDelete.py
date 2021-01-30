from timeit import Timer
from random import randrange

"""
--- Compare Deletion (del) for Lists vs Dicts ---
Runs a test to compare the performance of the deletion operator on a list and a dictionary.
List del is on average O(n) because subsequent elements need to be moved, while for dicts it is O(1)
because of the way they are implemented (i.e. as a hash table).
"""


def testDel(list_or_dict, i):
    del list_or_dict[i]
    return list_or_dict


# test the operations on increasingly large lists to measure time complexity
for listSize in range(1000, 10001, 1000):
    listTotal, dictTotal = 0, 0
    for trial in range(1000):  # 1000 trials for a more accurate average time
        # list made out of random values from 0 to 10000
        numsList = [randrange(0, 10000) for i in range(listSize)]
        # dictionary made out of keys 0, 1, 2, etc so that a random key can be generated and we will never get a KeyError.
        # we fill it with random values from 0 to 10000
        numsDict = {i: randrange(0, 10000) for i in range(listSize)}
        # assigning the random index separately instead of inline so it doesn't interfere with timing.
        randIndex = randrange(0, listSize-1)
        # time the del operation on our list
        listTimer = Timer("testDel(numsList, randIndex)", "from __main__ import testDel, numsList, randIndex")
        listTotal += listTimer.timeit(1)
        # repeat the process for the dictionary
        dictTimer = Timer("testDel(numsDict, randIndex)", "from __main__ import testDel, numsDict, randIndex")
        dictTotal += dictTimer.timeit(1)
    # print summary of information
    print(f"size: {listSize} --- list time: {listTotal} --- dictionary time: {dictTotal}")
