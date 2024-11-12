# Negative Index list slice

# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.

a = [1,2,3,4,5]
print(a[-4:-2])  # Not include -1 index and end upto -2 to -4
print(a[1:-1])  # index -2 = 4 and index 1 = 2, output will be [2,3,4]
print(a[1:-2])
print(a[0:5])
print(a[0:]) # End upto end of list
print(a[:3]) # start with 0

#about the del instruction
del a[0:2] # It will delete index 0:1
print(a)
# Deleting all the elements at once is possible too:
del a[:]
print(a)