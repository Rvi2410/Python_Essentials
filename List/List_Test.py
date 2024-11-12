row = []

#for i in range(8):
row = ["WHITE_PAWN" for i in range(8)]
    #row.append("WHITE_PAWN")
print(row)

#############################
squares = [x ** 2 for x in range(10)]
print(squares)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)