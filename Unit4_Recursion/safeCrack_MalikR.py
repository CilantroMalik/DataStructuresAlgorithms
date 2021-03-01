"""
--- SafeCrack ---
Password validator and brute-force cracker. Has two main functionalities: a function that checks whether a given password
is valid according to a set of specifications, and a function that uses brute force to guess a user's password by trying
combinations until it finds a password that exactly matches.
"""

from getpass import getpass
import random
import os
import time

# -- VALIDATOR --


# checks a user's password for validity based on the following conditions:
# -> between 6 to 18 characters in length
# -> contains at least 2 uppercase letters
# -> contains at least 1 lowercase letter
# -> contains at least 2 numbers
# -> contains at least 1 special character
# -> has no more than 3 consecutive appearances of the same character
# @param password: the password string to validate
def validate(password):
    # call our helper function with all the necessary starting parameter values. also do the initial length check
    # right now because we might as well, and exit out immediately if the password fails this
    if 6 <= len(password) <= 20:
        return validateHelper(password, 0, [0, 0, 0, 0], [" ", 0])
    else:
        print(f"Invalid: password is too {'long' if len(password) < 6 else 'short'} (must be 6-20 characters in length)")
        return False


# helper function that does all the work of validating the password; uses parameters to store information through recursion
# @param password: the password string to validate
# @param i: the current index we are looking at (we go through the password character by character)
# @param reqs: a list of four numbers keeping track of the four types of character requirements. It starts as [0, 0, 0, 0]
#              for [upper, lower, digit, special] and the relevant value is incremented each time it appears in the string.
# @param inRow: a list of two items, a character and a number, keeping track of how many instances of a character appear
#               consecutively. The variable starts at [" ", 0] and the counter is reset every time a new character is encountered
#               but incremented if the currently stored character is encountered again.
def validateHelper(password, i, reqs, inRow):
    if i == len(password):  # this means we have reached the end of the password; now just check the requirements
        if reqs[0] >= 2 and reqs[1] >= 1 and reqs[2] >= 2 and reqs[3] >= 1:
            return True  # requirements are met and we have not exited out previously due to repeated chars --> we are done
        else:
            print("Invalid: missing requirements (need 2 uppercase, 1 lowercase, 2 digits, 1 special character)")
            return False

    if password[i] != inRow[0]:  # each time, check for repeated chars; if this is a new char, reset the repetition tracker
        inRow[0], inRow[1] = password[i], 1
    else:  # if a repeated char, increment the repetition tracker, but if it is already at 2, the password must be invalid
        if inRow[1] == 2:
            print("Invalid: more than two of the same character in a row")
            return False
        inRow[1] += 1

    # check for each of the requirements and increment the relevant indices of the requirement tracker
    if password[i].isupper():
        reqs[0] += 1
    elif password[i].islower():
        reqs[1] += 1
    elif password[i].isdigit():
        reqs[2] += 1
    else:
        reqs[3] += 1

    return validateHelper(password, i + 1, reqs, inRow)  # call our function recursively, incrementing the index by 1


# -- CRACKER --

# helper variable for brute forcing. indices -> uppercase: 0-25; lowercase: 26-51; numbers: 52-61; special chars: 62-84
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+<>?:\"[]{}|."


# "brute force" cracker, but allows access to individual characters in the string
# @param password: the target password to be guessed
# @param verbose: optional parameter, if set to True the brute force cracker will periodically output its guesses
def bruteForce(password, verbose=False):
    # call our helper function with a few extra parameters: the list storing our guess (list for fast operations) and the
    # index we are currently at, which we need to keep track of our place through recursion. we additionally have to pass
    # in a list of one item, storing the number of tries (starting at zero) - we use a list because they are passed by reference
    # unlike integers and therefore their value persists across recursive calls. finally, we pass through the verbose option.
    return bruteForceHelper(password, [""] * 20, 0, [0], verbose)


# helper function that performs the brute forcing; parameters discussed above
def bruteForceHelper(password, guess, i, tries, verbose=False):

    try:  # try to access the element at i; if we cannot, that means we have reached the end of the list and should return
        _ = password[i]
    except IndexError:
        # have to convert "guess" from a list back to a string, then check it against password even though this is slightly
        # redundant (as due to our method we already know this is true in the ideal case). we return the number of tries.
        return tries[0] if "".join(guess) == password else None  # slightly redundant check because ideally we will already know this is true

    for char in chars:  # go through each possible character to check if it matches the character at the current position in the password
        if verbose:  # first, if we are in verbose mode, we want to print out the current guess for visible progress
            print("".join(guess[:i]) + randomChars(random.randint(3, 7)))  # add some randomness to add a little noise and make it realistic
            time.sleep(0.01)  # so the guesses don't flash by imperceptibly quickly
            os.system("clear")  # clear the terminal each time so guesses show up on the same line instead of in sequence; looks better this way

        tries[0] += 1  # each time we run the below if statement, we are checking against the password, so add 1 to tries
        if password[i] == char:
            guess[i] = char
            break  # we can quit the loop after we have found the character we want
    return bruteForceHelper(password, guess, i + 1, tries, verbose)  # we have incrementally improved our guess; now move onto the next character


# helper function that generates a sequence of random characters of the given length
# @param numChars: the number of random characters to generate
def randomChars(numChars):
    output = ""  # create a string to accumulate with characters
    for i in range(numChars):
        output += chars[random.randint(0, 84)]  # add a random character from the list (generate a random index)
    return output  # then return our string that we built up


# --- main program interface ---
print("Welcome to SafeCrack")
while True:  # main loop; has to be "while True" because the user can go on indefinitely
    pwd = getpass(prompt="Enter a password: ")  # get the user's password securely
    print("Validating...")
    if validate(pwd):  # if the password is valid, give feedback and move on to cracking
        print("Valid!")
        input("Press enter to proceed to cracking...")  # wait for user feedback before proceeding
        time.sleep(1)  # contributes to the realism a little bit
        os.system("clear")  # prepare for the cracker
        print(f"Guessed {pwd} in {bruteForce(pwd, True)} tries")  # call the brute force method, with verbose mode on

    if input("Press enter to run this utility again, or type any key to quit.") != "":  # no error handling needed because it is so broad
        break  # if the user wanted to exit (anything but empty) then exit the loop
print("Goodbye")
