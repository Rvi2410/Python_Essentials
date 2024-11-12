block=int(input("Enter the total no of blocks : "))
#print(block)
height = 0
current_level = 0

while block  >= current_level:
    block -= current_level
    #print(block)
    current_level += 1
    #print(current_level)
height = current_level - 1
print(height)