# Print function
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

###################################

# You need to define it. The word define is significant here.
# This is what the simplest function definition looks like:

def function_name():
    function_body

# It always starts with the keyword def (for define)
# next after def goes the name of the function (the rules for naming functions are exactly the same as for naming variables)
# after the function name, there's a place for a pair of parentheses (they contain nothing here, but that will change soon)
# the line has to be ended with a colon;
# the line directly after def begins the function body ‒ a couple (at least one) of necessarily nested instructions,
# which will be executed every time the function is invoked; note: the function ends where the nesting ends, so you have to be careful.

############################################################
def messgae():
    print("Enter a Value: ")

print("Start")
print("End")

# Note: we don't use the function at all ‒ there's no invocation of it inside the code.
# Output : Start End

# Insert function between your code

print("Start")
messgae()  # message() function will be called and executed here
print("End")

# => When you invoke/call a function, Python remembers the place where it happened and jumps into the invoked/called function;
# => The body of the function is then executed;
# => Reaching the end of the function forces Python to return to the place directly after the point of invocation.
# => Function must be defined before its execution, else gives error

################################################
# Assigning a value to the name message causes Python to forget its previous role. The function named message becomes unavailable.
#
# Fortunately, you're free to mix your code with functions ‒ you're not obliged to put all your functions at the top of your source file.

def message():
    print("Enter a value: ")

message = 1 #message value will be updated to 1, code will forgot old value/instruction given for message function

##########################################################
# A parameter is actually a variable, but there are two important factors that make parameters different and special:

# parameters exist only inside functions in which they have been defined, and the only place where the parameter can be defined is a space between a pair of parentheses in the def statement;
# assigning a value to the parameter is done at the time of the function's invocation, by specifying the corresponding argument.

def function(parameter):
    print(parameter)

# Don't forget:
# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters

##################################################
#Let's modify the function ‒ it has two parameters now:

def message(what, number):
    print("Enter", what, "number", number)

message("Even", 24)
message("Odd", 3)
message("Telephone", "Number")



