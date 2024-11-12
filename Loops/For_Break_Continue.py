print("Break the execution")
for i in range(10):
    if i == 3:
        break
    print("Inside the loop, i = ", i)
print("outside the loop")

print("Break the execution")
for i in range(10):
    if i >= 4:
        continue
    print("Inside the loop, i = ", i)
print("outside the loop")
