#Scenario

# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history.
# Some people consider them to be the most influential act of the rock era. Indeed,
# they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

# The band underwent many line-up changes, culminating in 1962 with
#    the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).

# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatels = []

beatels.append("John Lennon")
print("1", beatels)
beatels.append("Paul McCartney")
print("2", beatels)
beatels.append("George Harrison")
print("3", beatels)

print(beatels)
#use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
for i in range(2):
    beatels.append(input("Enter the singer name : "))
print(beatels)

beatels.remove("Ravi") #remove Ravi
print(beatels)
beatels.remove("Bhargav") #remove Bhargav
print(beatels)
beatels.insert(0,"Ringo Starr") #insert Ringo at 0 index
print(beatels)
