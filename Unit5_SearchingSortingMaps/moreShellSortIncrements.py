import random
import time


# main shell sort function: takes in the list to be sorted, and then a list of increments to be successively used
def shellSort(alist, increments):
    for gap in increments:
        for start in range(gap):
            gapInsertionSort(alist, start, gap)


# helper function for readability: extracts the insertion sort functionality and adds the gap
def gapInsertionSort(alist, start, gap):  # insertion sort, but taking the gap into account
    for i in range(start + gap, len(alist), gap):  # range object that skips numbers with the given interval

        currentvalue = alist[i]
        position = i
        # sort as normal, scanning through the list and updating the position value as we go
        while position >= gap and alist[position - gap] > currentvalue:  # have to decrement by 'gap' instead of 1
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue  # same as normal insertion sort


# function that times the execution of the given function
def checkTime(func):
    testList = random.sample(range(100000), 10000)  # random list of length 10000 containing any numbers up to 100000
    incSets = [
        [2 ** k + 1 for k in range(13, -1, -1)],  # sort of Mersenne numbers
        [2 ** k - 1 for k in range(13, -1, -1)],  # actual Mersenne numbers
        [4 ** k + 3 * (2 ** (k - 1)) + 1 for k in range(6, 0, -1)] + [1],
        # numbers of the form 4^k + 3*2^k + 1, ending with 1
        [int(10000 / (2 ** k)) for k in range(1, 14)],  # dividing the length of the list by successive powers of 2
        [(3 ** k - 1) // 2 for k in range(8, 0, -1)]  # numbers of the form (3^k - 1) / 2
    ]
    incSetTimes = [0, 0, 0, 0, 0]  # keep track of total time for each increment set
    for i in range(10):  # run 100 tests to begin to smooth out averages and invoke the Law of Large Numbers
        for i, set in enumerate(incSets):  # test for each increment set
            start = time.time()
            for _ in range(25):  # 25 trials to mitigate small number uncertainties
                func(testList, set)
            incSetTimes[i] += time.time() - start  # add the delta-time to the corresponding total

    for set, elapsedTime in zip(incSets, incSetTimes):
        print(f"Average Shell Sort (Inc = {set}) Time: {round(elapsedTime / 250, 8)}")


checkTime(shellSort)
