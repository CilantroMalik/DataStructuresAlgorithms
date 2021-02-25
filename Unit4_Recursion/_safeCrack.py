"""
--- SafeCrack ---
Password validator and brute-force cracker. Has two main functionalities: a function that checks whether a given password
is valid according to a set of specifications, and a function that uses brute force to guess a user's password by trying
combinations until it finds a password that exactly matches.
"""

from timeit import Timer
from getpass import getpass
import random
import os
import time

# -- validator --

# checks a user's password for validity based on the following conditions:
# -> between 6 to 18 characters in length
# -> contains at least 2 uppercase letters
# -> contains at least 1 lowercase letter
# -> contains at least 2 numbers
# -> contains at least 1 special character
# -> has no more than 3 consecutive appearances of the same character
# @param password: the password string to validate
def validate(password):
    return validateHelper(password, 0, [0, 0, 0, 0], [" ", 0]) if 6 <= len(password) <= 15 else False


# helper function that does all the work of validating the password; uses parameters to store information through recursion
# @param password: the password string to validate
# @param i: the current index we are looking at (we go through the password character by character)
# @param reqs: a list of four numbers keeping track of the four types of character requirements. It starts as [0, 0, 0, 0]
#              for [upper, lower, digit, special] and the relevant value is incremented each time it appears in the string.
# @param inRow: a list of two items, a character and a number, keeping track of how many instances of a character appear
#               consecutively. The variable starts at [" ", 0] and the counter is reset every time a new character is encountered
#               but incremented if the currently stored character is encountered again.
def validateHelper(password, i, reqs, inRow):
    if i == len(password):
        return reqs[0] >= 2 and reqs[1] >= 1 and reqs[2] >= 2 and reqs[3] >= 1

    if password[i] != inRow[0]:
        inRow[0], inRow[1] = password[i], 1
    else:
        if inRow[1] == 2:
            return False
        inRow[1] += 1

    if password[i].isupper():
        reqs[0] += 1
    elif password[i].islower():
        reqs[1] += 1
    elif password[i].isdigit():
        reqs[2] += 1
    else:
        reqs[3] += 1

    return validateHelper(password, i + 1, reqs, inRow)


# -- cracker --

# helper variable for brute forcing. indices -> uppercase: 0-25; lowercase: 26-51; numbers: 52-61; special chars: 62-84
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+<>?:\"[]{}|."


# uses brute force to attempt to guess the user's password, having only access to check an entire guess for equality
# @param password: the target password to be guessed
def bruteForce(password):
    # have to test for each possible length of password from 6 to 15
    for i in range(6, 16):
        # call our main function with the password as a list for faster operations, the length as a parameter (for speed),
        # our guess for the password (starts as all Qs, implemented as a list for faster get/set), the index we are
        # currently at, which will keep track of recursion, and finally the number of tries (again as a list so it persists
        # through recursion since lists are passed by reference but integers are not).
        result = bruteForceHelper(list(password), i, ["Q"] * i, 0, [0])
        if result is not None:  # if this length returned a match, we are done; if not, just try the next length
            return result[0]


# main function that does all the work; parameters discussed above
def bruteForceHelper(password, length, guess, i, tries):
    if i == length:  # if we have reached the end of the list in our recursion, check whether the guess was correct
        tries[0] += 1  # since we are checking we have to add one try
        return tries if guess == password else None
    for char in chars:  # at each iteration, we go through every possible character that could be in the position
        if guess[i-1] == char and guess[i-2] == char:  # if this would be the third character in a row, skip this branch
            continue
        guess[i] = char  # set the character of the guess to the current letter we are on
        result = bruteForceHelper(password, length, guess, i + 1, tries)  # "branch" off into a new function call with this letter
        if result is not None:  # if we received a match from this "branch", we are done, if not, try another branch
            return result
    return None  # if we did not receive a match from any letter in this branch, we made a mistake somewhere up the tree


# new "brute force" cracker that allows access to individual characters in the string
# @param password: the target password to be guessed
# @param verbose: optional parameter, if set to true the brute force cracker will periodically output its guesses
def newBruteForce(password, verbose=False):
    # call our helper function with a few extra parameters: the list storing our guess (list for fast operations) and the
    # index we are currently at, which we need to keep track of our place through recursion
    return newBruteForceHelper(password, [""]*16, 0, [0], verbose)


# helper function that performs the brute forcing; parameters discussed above
def newBruteForceHelper(password, guess, i, tries, verbose=False):

    try:  # try to access the element at i; if we cannot, that means we have reached the end of the list and should return
        _ = password[i]
    except IndexError:
        result = "".join(guess)  # convert from a list back to a string
        return tries[0] if result == password else None  # slightly redundant check because ideally we will already know this is true

    for char in chars:  # go through each possible character to check if it matches the character at the current position in the password
        if verbose:
            print("".join(guess[:i]) + randomChars(random.randint(3, 7)))
            time.sleep(0.01)
            os.system("clear")

        tries[0] += 1
        if password[i] == char:
            guess[i] = char
            break  # we can quit the loop after we have found the character we want
    return newBruteForceHelper(password, guess, i+1, tries, verbose)  # we have incrementally improved our guess; now move onto the next character


def randomChars(numChars):
    output = ""
    for i in range(numChars):
        output += chars[random.randint(0, 84)]
    return output


# --- testing ---
# print(validate("ABc12!"))
# print(validate("1!2qwEE"))

# timer = Timer("bruteForce('3p!c')", "from __main__ import bruteForce")
# print("done in", timer.timeit(1), "seconds")

# print(newBruteForce("BNFIgh145$%&"))

# --- main program interface ---
print("Welcome to SafeCrack")
print("Are you looking to validate a password (v) or attempt to crack one (c)?")
task = input("(Type 'v' or 'c'.) ")
password = getpass(prompt=f"Enter password to {'validate' if task == 'v' else 'crack'}: ")
if task == "v":
    print("Valid" if validate(password) else "Invalid")
elif task == "c":
    os.system("clear")
    print(f"Guessed {password} in {newBruteForce(password, True)} tries")
