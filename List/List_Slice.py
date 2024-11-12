# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2

list_1 = [1,2,3,4]
# my_list[start:end]
# A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from "start" to "end - 1".
print(list_1[:])
print(list_1[0:2])
list_2 = list_1[2:4]  # (start) :  (end-1)
print(list_2)

#about the del instruction
a = [1,2,3,4]
del a[0:1] # It will delete index 0:2
print(a)
# Deleting all the elements at once is possible too:
del a[:]
print(a)