def message():
    print("Enter a Value: ")

print("Start")
print("End")

# Note: we don't use the function at all ‒ there's no invocation of it inside the code.
# Output : Start End

# Insert function between your code

print("Start")
message()  # message() function will be called and executed here
print("End")

# => When you invoke/call a function, Python remembers the place where it happened and jumps into the invoked/called function;
# => The body of the function is then executed;
# => Reaching the end of the function forces Python to return to the place directly after the point of invocation.
# => Function must be defined before its execution, else gives error

#########################################################
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

################################
def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

##########################################
def message(number):
    print("Enter a number:", number)
number = 1234
message(10)
print(number)
number = int(input("Enter a Number :"))
message(number)






