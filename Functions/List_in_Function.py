 #  may a list be sent to a function as an argument?

 # if you pass a list to a function, the function has to handle it like a list.

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

# print(list_sum(5)) will give an Error

def new_list_fun(n):
    new_list = []

    for i in range(n):
        new_list.append(i)
    return new_list

print(new_list_fun(5))