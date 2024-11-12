my_list = ["A","B","C","D"]
char = 0

for i in range(len(my_list)):
    char = my_list[i]
    #print(char)
    for i in range(len(my_list)):
        #print(char,my_list[i])
        pair = char + my_list[i]
        print(pair)