from timeit import Timer
from random import randrange

"""
--- FindMin ---
Comparison between two methods of finding the minimum item in a list, one which compares
every item to every other item, for a complexity of O(n^2), and another which only iterates
through the list once, for a complexity of O(n). The two implementations are then compared
in a timed test on increasingly large samples of random integers.
"""


# find minimum item in a list in O(n^2)
def inefficientFindMin(nums):
    current_min = nums[0]  # at the start, default the minimum to the first item of the list
    for num in nums:
        is_min = True  # for each number, see if it is the smallest number
        for other in nums:
            if other < num:  # i.e. if there is no number less than it in the list
                is_min = False  # if there is, this number is not the minimum
        if is_min:  # if it is the smallest number, store that information
            current_min = num
    return current_min  # finally, return the stored smallest number


# find minimum item in a list in O(n)
def findMin(nums):
    current_min = nums[0]  # as before, the minimum starts as the first item
    for num in nums:
        if num < current_min:  # check every number, and if it is lower, update current_min
            current_min = num
    return current_min  # then return the variable, which will now store the lowest number


# time comparison between the two approaches on relatively large lists
for listSize in range(1000, 10001, 1000):  # try it 10 times for longer and longer lists, to see how performance scales
    nums = [randrange(0, 10000) for i in range(listSize)]  # random list of integers <= 10000, of increasing length
    # first create and run a timer for the inefficient O(n^2) version, then print the results
    timer1 = Timer("inefficientFindMin(nums)", "from __main__ import inefficientFindMin, nums")
    print(f"size: {listSize}, time for O(n^2): {timer1.timeit(3)}")
    # then repeat the same process for the O(n) implementation
    timer2 = Timer("findMin(nums)", "from __main__ import findMin, nums")
    print(f"size: {listSize}, time for O(n): {timer2.timeit(3)}")
