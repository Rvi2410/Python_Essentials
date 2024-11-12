# To get functions to return a value (but not only for this purpose) you use the return instruction.
#
# This word gives you a full picture of its capabilities. Note: it's a Python keyword.
#
# The return instruction has two different variants ‒ let's consider them separately.

# Return without an expression

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year")

# Return with an expression
def function():
    return 123 #expression

####################################
def function():
    return 123

x = function() # Invoc/Call the function with return value 123

print("Function Return value is", function())  # Invoc/Call the function with return value 123

#############################################

def boring_function():
    print("Boredome Mode' ON.")
    return 123

print("This lesson is Interesting!")
boring_function()                                       # Invoc/Call the boring_function with return print function
print("Functiona Call", boring_function())            # Invoc/Call the boring_function with return its value 123
print("This lesson is Board...")

##############################################



