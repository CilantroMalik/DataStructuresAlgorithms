from timeit import Timer
from random import randrange


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
