#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main script execution
if __name__ == "__main__":
    # Convert the first command-line argument to an integer and calculate its factorial
    f = factorial(int(sys.argv[1]))
    # Print the result
    print(f)
