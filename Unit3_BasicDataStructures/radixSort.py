import math
import random

listToSort = random.sample(range(1000), 10)


def radix(alist):
    # take the log base 10 then floor it to get the nearest power of 10
    # lower than the number, which is one less than the number of digits
    # that the number has, because of how powers of 10 start from zero.
    # and do this for the maximum number so we get the max number of digits
    maxDigits = math.floor(math.log10(max(alist))) + 1

    for i in range(maxDigits):  # as many passes as digits
        # create our digit bins: a list of 10 lists, each representing one bin
        digitBins = [[] for i in range(10)]

        # this will get the desired digit of the number
        # depending on which pass we are on
        # by floor-dividing it by the corresponding power of 10
        # which has the effect of truncating the number, such that
        # the last digit is the one we want, then we can extract
        # that digit using a modulo by 10
        getDigit = lambda x: x // (10 ** i) % 10

        # put the numbers in bins based on the relevant digit,
        # as found by the lambda function above
        # note: the list passed in as a parameter functions as the main bin
        for num in alist:
            digitBins[getDigit(num)].append(num)
        alist = []  # clear the main bin for refilling
        # now refill the main bin
        for bin in digitBins:
            alist += bin  # the concatenation preserves order

    return alist
