"""
The keys() method
Can dictionaries be browsed using the for loop, like lists or tuples?
=> No and yes.
=> No, because a dictionary is not a sequence type − the for loop is useless with it.
=> Yes, because there are simple and very effective tools that can adapt any dictionary to the for loop requirements
(in other words, building an intermediate link between the dictionary and a temporary sequence entity)
"""

##################################################
# 1) keys() Method : The method returns an iterable object consisting of all the keys gathered within the dictionary.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "=>", dictionary[key])

#####################################################
# 2) items() : The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair

for english, french in dictionary.items(): # Here english is key and french is its value
    print(english, "->", french)

for key, value in dictionary.items():
    print(key, "->", value)

########################################################
# 3) Modifying and adding values in dictionary

dictionary = {"Ravi":"Dholariya", "Bhargav":"Rathod", "Vikash":"Yadav"}

print(dictionary)
dictionary["Ravi"] = 'Patel'
print(dictionary)

#####################################################
# 4) Shorted

dictionary = {"Ravi":"Dholariya", "Bhargav":"Rathod", "Vikash":"Yadav"}
dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

for key in sorted(dictionary.keys()):  # Sorted by alphabet
    print(key)
for key in sorted(dictionary_2.keys()):  # Keys sorted by numbers
    print(key)

#####################################################
# 5) values

dictionary = {"Ravi":"Dholariya", "Bhargav":"Rathod", "Vikash":"Yadav"}
dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

print(dictionary.values())
for value in sorted(dictionary.values()):  # Value will be sorted by Alphabet
    print(value)
for value in sorted(dictionary_2.values()):  # Value will be sorted by Alphabet
    print(value)

#####################################################
# 6) Add new key

dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

dictionary_2[4] = "Four"

print(dictionary_2)

#####################################################
# 7) Add new key using .update()

dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

dictionary_2.update({5:"Five"})
print(dictionary_2)

#####################################################
# 8) Del a key

dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

del dictionary_2[2]
print(dictionary_2)

#####################################################
# 9) popitem()
# => It will pop/store and delete last item from dictionary

dictionary_2 = {2:"One", 3:"Two", 0:"Three"}

dictionary_2.popitem() # remove last item of the dictionary
print(dictionary_2)

#####################################################
#10) clear() // To remove all the dictionary's items, you need to use the clear() method:

dictionary_2 = {2:"One", 3:"Two", 0:"Three"}
dictionary_2.clear() # It will clear the dictionary
print(dictionary_2)

##################################################
# 11) Convert Tupple to Dictionary

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)
