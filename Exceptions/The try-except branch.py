"""
So, we could say that these two blocks work like this:

1) "try" keyword marks the place where you try to do something without permission;
=>first, starting with the try keyword – this is the place where you put the code you suspect is risky and may be terminated in case of error;
=> note: this kind of error is called an exception,
=> while the exception occurrence is called raising – we can say that an exception is (or was) raised;

2) "except" keyword starts a location where you can show off your apology talents.
=> second, the part of the code starting with the except keyword is designed to handle the exception;
it's up to you what you want to do here: you can clean up the mess or you can just sweep the problem under the carpet (although we would prefer the first solution).

"""

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)  # If error will come here program will execute except
except:
    print('I do not know what to do.')

####################################################
"""
Two exceptions after one try
ZeroDivisionError and ValueError

# Additionally, the number of except branches is not limited – you can specify as many or as few of them as you need, 
    but don't forget that none of the exceptions can be specified more than once.

"""

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.') # Program will take two execiton error
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')

###################################################
"""
The default exception and how to use it
"""
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

###################################################
"""
Some Useful exceptions
"""
"""
1) ZeroDivisionError

=> This appears when you try to force Python to perform any operation which provokes division in which the divider is zero,"
=> or is indistinguishable from zero. Note that there is more than one Python operator which may cause this exception to raise. Can you guess them all?

=> Yes, they are: /, //, and %.
"""
try:
    value = 0
    print("Zero Division", 1 / value)
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')

"""
2) ValueError
=> Error will raise when invalide input/value has been given then expected
=> i.e.: If user has added "String" value instead of integer value
"""
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('Please enter correct integer value')

"""
3) TypeError
=> This exception shows up when you try to apply a data whose type cannot be accepted in the current context. Look at the example:
"""
try:
    short_list = [1]
    one_value = short_list[0.5]  # Here it is expected to be index number in short_list[]
except TypeError:
    print("It is Type error")

"""
AttributeError
This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an item you're dealing with. For example:
"""
try:
    short_list = [1]
    short_list.append(2)
    short_list.depend(3) #there is no depend method in list
except TypeError:
    print("It is AttributeError ")

"""
Indentation Error
IndentationError: unexpected indent:Unexpected Space and tab has been given in code
"""
try:
    short_list = [1]
        short_list.append(2)
except IndentationError:
    print("It is Indentation Error")

"""
SyntaxError
=> Sytex is incorrect
i.e: print("Hello,world!) 
    => Here print data should be in-between "", else it gives a SyntaxError

Name error
=> Name error if inbuilt function
"""
