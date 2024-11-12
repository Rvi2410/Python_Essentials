numbers = [10, 5, 7, 2, 1]
print(numbers)
print(len(numbers))
numbers.append(10) #It takes its argument's value and puts it at the end of the list which owns the method.
print(numbers)
numbers.insert(4,12) #The insert() method is a bit smarter ‒ it can add a new element at any place in the list, not only at the end.
print(numbers)
my_list = []  # Creating an empty list.

# append using for loop
for i in range(5):
    my_list.append(i + 1)

print(my_list)