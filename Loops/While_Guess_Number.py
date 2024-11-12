secret_number = 24
number = int(input("Guess the number : "))
counter = 6

while counter != 0:
    if number != secret_number:
        print("Retry ",counter - 1)
        counter -= 1
        if counter == 1:
            print("You have reached Max number attempts")
            exit()
        number = int(input("Guess the number : "))
    else:
        print(number, "is correct number")
        exit()
