"""
Dictionary:
=> prefer to use curly brackets {}

Dictionary = {"Key" = "Value"}
For each element is defined as Key and it's value under the dictionary

"""
###################################
# For Example:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary["cat"])    # It will print value of key "cat" = "Chat"
print(phone_numbers["Suzy"]) # It will print value of key "Suzy" = 22657854310

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "=>", dictionary[word])
    else:
        print(word, "is not in dictionary")