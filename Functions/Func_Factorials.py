"""
Factorial

Factorial of n number = n (n-1)!....

0s factorial is 1
1s factorial is 1
4! = 4 x 3 x 2 x 1

"""

def factorial_number(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


n  = int(input("Enter a Number : "))

print(factorial_number(n))

for i in range(1,n+1):
    print(i, factorial_number(i))

