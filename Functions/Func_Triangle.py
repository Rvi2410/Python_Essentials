"""
Equilateral Triangle

Check whether three sides of given lengths can builds a Triangle.

It won't be a hard challenge. The function will have three parameters ‒ one for each side.

It will return True if the sides can build a triangle, and False otherwise.
In this case, is_a_triangle is a good name for such a function.

"""

def is_a_triangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(5,4,10))
print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))
print(is_a_triangle(2,2,2))

###########################################
def is_a_triangle(a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))
print(is_a_triangle(2,2,2))

###########################################
def is_a_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))
print(is_a_triangle(2,2,2))

#################################################
"""
Find Area of Triagle 

i) Heron's formula
s = a+b+c / 2
Area = √s(s-a)(s-b)(s-c)
In Python Area = (s * (s-a) * (s-b) * (s-c) ) ** 0.5

"""
def is_a_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

def area(a,b,c):
    s = (a + b + c) / 2
    return (s*  (s-a) * (s-b) * (s-c )) ** 0.5

def area_of_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    return area(a,b,c)

a  = float(input("Enter a first\'s side : "))
b  = float(input("Enter a first\'s side : "))
c  = float(input("Enter a first\'s side : "))
print(area_of_triangle(a, b, c))

