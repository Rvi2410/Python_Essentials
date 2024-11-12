temps = [[0.0 for h in range(24)] for d in range(31)]
print(temps)

#Here's an example of a list comprehension ‒ the code creates a five-element list filled with the first five natural numbers raised to the power of 3:

number = [num ** 3 for num in range(5)]
print(number)

# 2. You can use nested lists in Python to create matrices (i.e., two-dimensional lists). For example:

table = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]

print(table)

print(table[0][4])