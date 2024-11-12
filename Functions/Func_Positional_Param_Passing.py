def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

#################################
# First name, Last name

def introduction(first_name, last_name):
    print("My Name is", first_name, last_name)

introduction("Bhargav","Rathod")
introduction("Vikash", "Yadav")
introduction("Ravi", "Dholariya")

def introduction(first_name, last_name="patel"):
    print("My Name is", first_name, last_name)
introduction("Ravi", "Dholariya") #Function will overwrite the new value of parameters

##################################################
# Keyword argument passing

introduction(first_name= "Ravi", last_name= "Dholariya")

# Of course, you mustn't use a non-existent parameter name.

# Basic Math by using function

def adding(a,b,c):
    print(a, "+", b, "+", c, "=", a + b + c)
    print(a, "-", b, "-", c, "=", a - b - c)

adding(1, 2, 3)

#######################################################
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

#########################################################
# Other Example:
#Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

############################################################
