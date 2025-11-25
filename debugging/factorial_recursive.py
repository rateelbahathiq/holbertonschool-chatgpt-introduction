#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
