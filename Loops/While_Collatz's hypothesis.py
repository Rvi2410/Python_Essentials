# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, go back to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

c0 = int(input("Enter any non-Zero, Positive integer number"))
step = 0

while c0 != 0:
    if c0 % 2 == 0:
        c0 = c0/2
        print(c0)
        step +=1
        if c0 == 1:
            print("Total step to reach =", step)
            exit()
    else:
        c0 = 3 * c0 +1
        print(c0)
        step += 1
        if c0 == 1:
            print("Total step to reach =", step)
            exit()
#exit()
