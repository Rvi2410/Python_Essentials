#if-else
#Read the two numbers
number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number: "))

print("Number1 = ", number1)
print("Number2 = ", number2)

# Choose the larger number
if number1 > number2:
    larger_number = number1
else :
    larger_number = number2

# Print the result
print("Larger number is : ", larger_number)