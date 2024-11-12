#if-else
#Read the three numbers
a = int(input("Enter the first number : "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("Number1 = ", a)
print("Number2 = ", b)
print("Number3 = ", c)

if a > b :
    larger_number = a
    if a > c:
        larger_number = a
elif b > c:
    larger_number = b
else:
    larger_number = c

print("Larger number is", larger_number)
larger_number = max(a,b,c)
print("Larger number is", larger_number)
lowest_number = min(a,b,c)
print("Lowest number is", lowest_number)