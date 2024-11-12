my_list = [17, 3, 11, 5, 1, 9, 7, 34, 13]
larger_number = 0

for i in range(len(my_list)):
    if my_list[i] > larger_number:
        larger_number = my_list[i]
print(larger_number)

# Another way
larger_number = 0
for i in my_list:
    if i > larger_number:
        larger_number = i
print(larger_number)