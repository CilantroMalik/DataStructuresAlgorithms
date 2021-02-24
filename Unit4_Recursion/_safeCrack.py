"""
--- SafeCrack ---
Password validator and brute-force cracker. Has two main functionalities: a function that checks whether a given password
is valid according to a set of specifications, and a function that uses brute force to guess a user's password by trying
combinations until it finds a password that exactly matches.
"""

from timeit import Timer

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


# helper variable for brute forcing. indices -> uppercase: 0-25; lowercase: 26-51; numbers: 52-61; special chars: 62-84
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+<>?:\"[]{}|."


# uses brute force to attempt to guess the user's password
def bruteForce(password):
    for i in range(2, 7):
        result = bruteForceHelper(list(password), i, ["Q"] * i, 0, [0])
        if result is not None:
            return result[0]
        print("finished", i, "letters")


def bruteForceHelper(password, length, guess, i, tries):
    if i == length:
        tries[0] += 1
        return tries if guess == password else None
    for char in chars:
        if guess[i-1] == char and guess[i-2] == char:
            continue
        guess[i] = char
        result = bruteForceHelper(password, length, guess, i + 1, tries)
        if result is not None:
            return result
    return None


# new "brute force" cracker that allows access to individual characters in the string
def newBruteForce(password):
    return newBruteForceHelper(password, [""]*16, 0)


def newBruteForceHelper(password, guess, i):
    try:
        _ = password[i]
    except IndexError:
        result = "".join(guess)
        return result if result == password else None

    for char in chars:
        if password[i] == char:
            guess[i] = char
            break
    return newBruteForceHelper(password, guess, i+1)


# --- testing ---
# print(validate("ABc12!"))
# print(validate("1!2qwEE"))

# timer = Timer("bruteForce('3p!c')", "from __main__ import bruteForce")
# print("done in", timer.timeit(1), "seconds")

print(newBruteForce("BNFIgh145$%&"))
