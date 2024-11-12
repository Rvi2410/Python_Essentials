# Pythagorean Theorem

# Equilateral Triangle

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a  = float(input("Enter a first\'s side : "))
b  = float(input("Enter a first\'s side : "))
c  = float(input("Enter a first\'s side : "))

if is_a_triangle(a,b,c):
    print('Yes, It can be a Triangle')
else:
    print("It can\'t be a Triangle")

##############################################
"""
Right Engle Triangle using Pythagorean Theorem

c2 = a2 + b2

"""

###############################################
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_engle_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    return c ** 2 == a ** 2 + b ** 2

a  = float(input("Enter a first\'s side : "))
b  = float(input("Enter a first\'s side : "))
c  = float(input("Enter a first\'s side : "))
print(is_a_triangle(a,b,c))
print(is_a_right_engle_triangle(a,b,c))

