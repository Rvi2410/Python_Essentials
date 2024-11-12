word = input("Enter any word : ")
print("Original word is ", word)
reverse_word = word[::-2]
print("Reverved word is :", reverse_word)

if reverse_word == word:
    print(word,"is a Palindrom word")
else:
    print(word,"is not a Palindrom word")