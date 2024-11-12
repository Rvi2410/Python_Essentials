"""
Function itself callled inside the function is called Function Recursion

Recursion is a technique where a function invokes itself.

The Fibonacci numbers definition is a clear example of recursion. We already told you that:

Fibi = Fibi-1 + Fibi-2
"""

##############################################
"""
Factorial Number using Recursion
"""

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

print(factorial_function(5))

###############################################