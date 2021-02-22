"""
--- SafeCrack ---
Password validator and brute-force cracker. Has two main functionalities: a function that checks whether a given password
is valid according to a set of specifications, and a function that uses brute force to guess a user's password by trying
combinations until it finds a password that exactly matches.
"""

# checks a user's password for validity based on the following conditions:
# -> between 6 to 18 characters in length
# -> contains at least 2 uppercase letters
# -> contains at least 1 lowercase letter
# -> contains at least 2 numbers
# -> contains at least 1 special characters
# @param password: the password string to validate
import time


def validate(password):
    return validateHelper(password, "length")


# helper function that recursively runs validation stage by stage (for each of the stipulations laid out above).
# @param password: passed straight through from the main function
# @param stage: what stage of validation the function is on (possible values: "len", "upper", "lower", "num", "spec")
def validateHelper(password, stage):
    if stage == "length":
        return validateHelper(password, "upper") if 6 <= len(password) <= 18 else False
    elif stage == "upper":
        return validateHelper(password, "lower") if len([c for c in password if c.isupper()]) >= 2 else False
    elif stage == "lower":
        return validateHelper(password, "num") if len([c for c in password if c.islower()]) >= 1 else False
    elif stage == "num":
        return validateHelper(password, "spec") if len([c for c in password if c.isdigit()]) >= 2 else False
    else:  # stage == "spec"
        return len([c for c in password if not (c.isalpha() or c.isdigit())]) >= 1


# TODO optimize this and maybe encode this info in function parameters
def validateAlt(password):
    diff = 0
    requirements = [1, 1, 1, 1]
    for char in password:
        if char.isupper():
            requirements[0] -= 1
        elif char.islower():
            requirements[1] -= 1
        elif char.isdigit():
            requirements[2] -= 1
        else:
            requirements[3] -= 1
    for req in requirements:
        diff += req if req > 0 else 0
    return diff


# indices -> uppercase: 0-25; lowercase: 26-51; numbers: 52-61; special chars: 62-84
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+<>?:\"[]{}|."


# uses brute force to attempt to guess the user's password
def bruteForce(password):
    for i in range(2, 7):
        result = bruteForceHelper(list(password), i, ["Q"] * i, 0, [0])
        if result is not None:
            return result[0]
        print("finished", i, "letters")


def bruteForceHelper(password, length, guess, i, tries):
    if validateAlt(guess) > length-i+1:
        return None
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


# --- testing ---
# print(validate("ABc12!"))
# print(validate("sbfhabSJ1342@#$"))
now = time.time()
print(bruteForce("3p!C"))
done = time.time()
print("guessed in", (done-now)//60, "min", (done-now) % 60, "sec")

