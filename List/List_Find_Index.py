my_list = [4,6,3,8,12,65,756,236,45,3,72,3,2,6,7,34,40]
find = int(input("Enter a number"))

for i in range(len(my_list)):
     if my_list[i] == find :
         print("Index", i)
     else:
        print(find, "is not at index", i)