"""
--- Recursive Fibonacci Sequence ---
Recursive implementation of the mathematical function F(n) which returns the nth number in the Fibonacci sequence,
which is defined recursively such that F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2).
"""


def fibonacci(n):
    if n == 0:  # base case 1: F(0) = 0
        return 0
    elif n == 1:  # base case 2: F(1) = 1
        return 1
    else:  # recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


''' 
performance of recursive vs iterative:
the recursive implementation of F(n) is quite slow for large n-values since you make two recursive calls for each layer. 
this makes the stack size grow exponentially as 2^n, which is extremely inefficient. with an iterative approach, 
one need only store a few variables and create a loop that iterates just under n times to increment the values.
the recursive approach in a vacuum is not much slower, since there are no high-time-complexity tasks per se, but
in reality it unnecessarily hogs memory, as compared to the iterative approach which has a much liwer space complexity.
'''