# Note:None is a keyword.
# There are only two kinds of circumstances when None can be safely used:
#
# when you assign it to a variable (or return it as a function's result)
# when you compare it with a variable to diagnose its internal state.

value = None
if value is None:
    print("Value is none")

# if a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None.

def function(n):
    if(n % 2 == 0):
        return True # For Even number, its return True, Else None

print(function(2))
print(function(1))
print(function(5))
print(function(10))