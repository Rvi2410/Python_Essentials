odd = 0
even = 0

number = int(input("Enter a number : "))

while number != 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    number = int(input("Enter a number : "))

print("Total odd numbers are : ", odd)
print("Total even numbers are :", even)
