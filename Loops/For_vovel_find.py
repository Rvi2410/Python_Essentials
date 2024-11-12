word = input("Enter a Word : ")
word= word.upper()
print(word)
print(len(word))
#word = "APPLE"
vovel = "AEIOU"
print(vovel[0:5])

print("Get Non-Vovel characters")
for i in word[0:]:
#    print(i)
     if i in vovel[0:]:
        continue
     else:
         print(i)

print("Get Vovel characters")
for i in word[0:]:
#    print(i)
     if i in vovel[0:]:
         print(i)
print(i[0:])

