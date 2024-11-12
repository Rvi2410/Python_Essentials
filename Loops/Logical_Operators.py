# And operator:
# counter > 0 and value == 100
# or operator:
# counter > 0 or value == 100
# not operator:

#Example
var = int(input("Enter any number : "))
print(var > 0)
print(var <= 0)
print(not(var <=0)) #not operatore, reverse the output
print(var != 0)
print(not (var == 0))

#######################################
i = 1
j = not not i
k = not i
print(i == j)
print(i != k)