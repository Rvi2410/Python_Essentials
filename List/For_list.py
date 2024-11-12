list = []

for i in range(10):
    list.append(i + 1)
print(list)

my_list = []  # Creating an empty list.

for i in range(10):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [1,2,3,4,5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]
print(total)

