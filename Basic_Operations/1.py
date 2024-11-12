a = "PAPA"
#print(a[4]==a[10])
print(int(len(a)))
b = a[0]
print(b)
for i in range(int(len(a)/2)):
    if a[i] == a[-i-1]:
        print(a[i], a[-i-1])
    else:
        print("a is not a palindrom")


