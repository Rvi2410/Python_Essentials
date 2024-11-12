

####################################
def is_prime(num):
    for i in range(2, num):
        prime = num % i == 0
        if prime == True:
            return False
    return True

for i in range(1, 200):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

###################################
a = int(input("Enter a number : "))

for i  in range(2, a):
    prime = a % i == 0
    if prime == True:
        print(a, "is not a prime number")
        exit()
    else:
        print(a, "is a prime number")
        exit()
