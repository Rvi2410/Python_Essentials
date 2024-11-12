#1. Print() Function:

print ("Hello World")
#i) \n : Data after \n will be print in new line
print("Hello \n World")

#ii) end=""
#Output will be continue of new print data after first line
#Any value/data put under end="" will be print after current print data
print ("Hello World", end="")
print ("Earth")
#output will be: Hello World Earth

#iii) sep=""
#printed data will be separated by given data in sep="" function
print("My", "name", "is", "Monty", "Python.", sep="-")
#output = My_name_is_Monty_Python.

#iv) Mixed sep="" and end=""
print("Programming","Essentials","in", sep="***", end="...")
print("Python \n Language")
#output: Programming***Essentials***in...Python
#         Language



