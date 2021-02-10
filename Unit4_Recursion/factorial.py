"""
--- Recursive Factorial ---
Simple implementation of the factorial function with a recursive approach. The factorial of n is defined as the product
of all natural numbers up to and including n and is often denoted with an exclamation mark (e.g. 4! = 4*3*2*1 = 24).
The factorial function is only defined for nonnegative integers.
"""

def factorial(n):
    if int(n) != n or n < 0:
        raise ValueError(f"factorial is undefined for input {n}")
    if n <= 1:  # 1! is obviously 1, and 0! is defined to be 1
        return 1
    else:  # recursive case: n times factorial of everything below it
        return n * factorial(n - 1)
