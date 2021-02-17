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
def validate(password):
    return validateHelper(password, "length")


# helper function that recursively runs validation stage by stage (for each of the stipulations laid out above).
# @param password: passed straight through from the main function
# @param stage: what stage of validation the function is on (possible values: "len", "upper", "lower", "num", "spec")
def validateHelper(password, stage):
    if stage == "length":
        return validateHelper(password, "upper") if 6 <= len(password) <= 18 else False
    elif stage == "upper":
        return validateHelper(password, "lower") if len([c for c in password if c.isalpha() and c == c.upper()]) >= 2 else False
    elif stage == "lower":
        return validateHelper(password, "num") if len([c for c in password if c.isalpha() and c == c.lower()]) >= 1 else False
    elif stage == "num":
        return validateHelper(password, "spec") if len([c for c in password if c.isdigit()]) >= 2 else False
    else:  # stage == "spec"
        return len([c for c in password if not (c.isalpha() or c.isdigit())]) >= 1


# uses brute force to attempt to guess the user's password
def bruteForce():
    pass


# --- testing ---
print(validate("ABc12!"))
print(validate("sbfhabSJ1342@#$"))
