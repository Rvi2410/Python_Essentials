"""
Tupple:
=> Tuples prefer to use parenthesis () or without any brackets
=> Whereas lists like to see brackets [],
=> Although it's also possible to create a tuple just from a set of values separated by commas.
"""

tupple_1 = (1,2,3,4)
tupple_2 = 1, 2.0, 0.35, 5.125

print(tupple_1)
print(tupple_2)

############################
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])      # Print index 0 tupple 1
print(my_tuple[-1])     # Print index -1 tupple 1000
print(my_tuple[1:])     # Print index 1 to n tupple = (10, 100, 1000)
print(my_tuple[:-2])    # Print index n to -2-1 = 10 = (1,10)

for elem in my_tuple:
    print(elem)
    print(elem)

"""
The similarities may be misleading − don't try to modify a tuple's contents! It's not a list!

Tupple can't be delete, modify, append, insert

"""
"""
What else can tuples do for you?

=> the 'len()' function accepts tuples, and returns the number of elements contained inside;
=> the '+' operator can join tuples together (we've shown you this already)
=> the '*' operator can multiply tuples, just like lists;
=> the 'in' and not in operators work in the same way as in lists.
"""

my_tuple = (1, 10, 100)
print(my_tuple)
t1 = my_tuple + (1000, 10000)
print(t1)
t2 = my_tuple * 3
print(t2)

print(my_tuple)
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

######################################
var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

##########################################
# Count Method
my_tuple = (1, 10, 100, 1000,1,1,1,2,4,5,1,2,1,2,3,1,3412,31,2,31,21,2,12,1,21,2)
duplicant = my_tuple.count(1)

print(duplicant)

####################################
# Convery list into Tupple

my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

########################################
# Convery Tupple to Dictionary

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)
