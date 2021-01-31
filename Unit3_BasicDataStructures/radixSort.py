import math

"""
--- Radix Sort ---
Implementation of the Radix Sort algorithm for lists, which sorts numbers based on individual digits,
going from lowest place value to highest and separating numbers into "bins" depending on the digit at that place
and then combining the bins in order to incrementally bring the list closer to being sorted.
Once every place value has been visited, the numbers will be completely sorted in ascending order.
"""


def radix(alist):
    # take the log base 10 then floor it to get the nearest power of 10 lower than the number, which is
    # one less than the number of digits that the number has, because of how powers of 10 start from zero.
    # do this for the maximum number in the list so we get the max number of digits
    maxDigits = math.floor(math.log10(max(alist))) + 1

    for i in range(maxDigits):  # as many passes as there are digits
        # create our digit bins: a list of 10 lists, each representing one bin.
        # (note: the list passed in as a parameter is being used as the main bin.)
        digitBins = [[] for i in range(10)]

        # now add each number to one of the digit bins based on the i-th digit from the right
        # (we retrieve it by floor-dividing by 10^i so the last digit is the desired one, then taking mod 10)
        # then we add our number to the bin corresponding to that digit
        for num in alist:
            digitBins[num // (10 ** i) % 10].append(num)

        # clear the main bin, then refill it with the values from the individual bins in order
        alist = []
        for aBin in digitBins:
            alist += aBin  # concatenation to the main list preserves order within each bin

    return alist
