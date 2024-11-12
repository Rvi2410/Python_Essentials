secret_number = 24
number = int(input("Guess the number : "))
#counter = 6

for counter in range(10):
    if number != secret_number:
        if counter != 4:
            print("Retry ",5 - counter)
            number = int(input("Guess the number : "))
            #continue
        else:
            print("Max Try")
            break
    else:
        print(number, "is correct number")
        break

