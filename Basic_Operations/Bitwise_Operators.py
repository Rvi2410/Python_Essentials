"""
Here are all of them:

 & (ampersand) ‒ bitwise conjunction;
 | (bar) ‒ bitwise disjunction;
 ~ (tilde) ‒ bitwise negation;
 ^ (caret) ‒ bitwise exclusive or (xor).
 """

a = 1
b = 2
#if a > 0 and b < 2
print( a and b)
print (a or b)
print(a & b)    # Binary AND
print( a | b)   # Binary OR
print(a ^ b)    # Binary XOR A'B + AB' //A' = Not A
print(~ a)   # Binaty NOT
a &= b
a |= b
a ^= b