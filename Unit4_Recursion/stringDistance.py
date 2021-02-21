"""
--- String Edit Distance Problem ---
Implementation of a solution to the string edit distance problem, which entails finding the lowest "cost" edit sequence
that transforms one string into another. Cost is calculated using the rules that adding or deleting a letter has a cost
of 20, and duplicating an already existing letter has a cost of 5. The function uses a recursive process to find all
letters that have to be added or deleted, then ones that have to be copied, and then propagating the cost up the stack.
The algorithm has to run twice and switch the order since edit distance is non-commutative, and simply takes the minimum.
"""

# main function, just finds the minimum of the two possible permutations of the strings (since the distance could be
# different in each case because adding, copying or deleting is dependent on the "first" string)
def stringDistance(str1, str2):
    return min(strDistHelper(str1, str2), strDistHelper(str2, str1))


# helper function that does all the work
def strDistHelper(str1, str2):
    # find all the letters we will have to add to string 2 (i.e. the ones that exist in string 2 but not in string 1)
    toAdd = [letter for letter in str2 if letter not in str1]
    if len(toAdd) > 0:  # add the letters we have to add, and add their cost, and then call the function again with added letters
        return strDistHelper(str1 + "".join(toAdd), str2) + 20 * len(toAdd)
    else:  # nothing left to add, now we look for copying
        toCopy = []
        for letter in str2:
            diff = str2.count(letter) - str1.count(letter)  # if there is more of a letter in one string than the other
            if letter not in toCopy and diff > 0:
                toCopy.extend([letter for _ in range(diff)])  # if there are two more copies in the second string, we have to add twice
        if len(toCopy) > 0:  # if there are letters to copy, add them to the string and add their cost, then recurse again
            return strDistHelper(str1 + "".join(toCopy), str2) + 5 * len(toCopy)
        else:  # finally we check for deletions
            # at this point, str2 is entirely contained in str1, now it only remains to delete letters that were not in the original string
            cost = 0
            for letter in str1:
                diff = [str1.count(letter), str2.count(letter)]  # letters that appear more in str1 than str2 -> ones that do not belong there
                if diff[0] > diff[1]:
                    str1 = str1.replace(letter, "", diff[0] - diff[1])  # replace the letter; set the replacement count to the difference
                    cost += 20 * (diff[0] - diff[1])  # add 20 to the cost for each deletion that occurs
            return cost  # return this so it propagates up the call stack


# testing (can replace with anything)
print(stringDistance("alligator", "algorithm"))

