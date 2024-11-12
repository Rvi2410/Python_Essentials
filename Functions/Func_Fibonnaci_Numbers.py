def fibonacci_sequence(n):
    if n < 1:
        return 0
    if n == 1:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(2, n +1):
        the_sum = elem_1 + elem_2
        elem_1 = elem_2
        elem_2 = the_sum
    return the_sum


n = int(input("Enter a number : "))
print("Fibonacci Squence for", n , "number is", fibonacci_sequence(n))

for n in range(1,n+1):
    print("Fibonacci Squence for", n, "number is", fibonacci_sequence(n))