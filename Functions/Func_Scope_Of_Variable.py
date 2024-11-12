def my_function():
    print("Do I know that variable?", var)


var = 1 # This variable will pe impactful after this define
my_function() # var veriable will be used under function as it is already defined
print(var)

# The answer is: a variable existing outside a function has scope inside the function's body.

def my_function():
    var = 2  #this is local variable applicable for this function only
    print("Do I know that variable?", var) # Here var value will be taken from local variable


var = 1 # This is global variable applicable in whole code
my_function()
print(var)

"""
There's a special Python method which can extend a variable's scope in a way which includes the function's body
(even if you want not only to read the values, but also to modify them).

Such an effect is caused by a keyword named global:

Global Variable value can be modify/update from function by using "global" keyword

global <name of the variable> // after this keyword variable value will be impacted to the global variable
"""

def my_function():
    global var
    var = 3  # var value will be updated to 3 in global variable
    print("Do I know that variable?", var)  # Here var value will be taken from local variable

var = 1  # This is global variable applicable in whole code
print(var) #Here var value will be 1 as defined
my_function()
print(var) #here var value will be 3 as it is updated inside function

################################################
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
