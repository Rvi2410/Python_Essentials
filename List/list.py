# the list starts with an open square bracket and ends with a closed square bracket; the space between the brackets is filled with five numbers separated by commas.
numbers= [10,45,6,9,3,1,6,8,9]
#positive index from left to right start with index 0
#Negative index from right to ledt start with index -1
print(len(numbers))
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
print(len(numbers))
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.
numbers[-1] = 222
print("New list contents: ", numbers)  # Current list contents.
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
print(numbers[0])
del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-1]) #Negative indexing
print(numbers[-3:-1]) #Negative indexing