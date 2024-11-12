#my_list = [1,2,3,4,5]
my_list = [8, 10, 6, 2, 4]
#my_list = [4, 10, 6, 2, 4,5,8,99,45,90,23,56,78,12,36,57]  # list to sort
length = len(my_list)

for i in range(len(my_list) - 1):
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            print(my_list)
print("Reversed list =", my_list)
            #print("Updated list in iteration ", i, "is", my_list)
#    print("Updated list in iteration ", j, "is", my_list)

########################################################
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

my_list = [8, 10, 6, 2, 4]
my_list.reverse()
print(my_list)