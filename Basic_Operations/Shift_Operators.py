"""
Python offers yet another operation relating to single bits: shifting.
This is applied only to integer values, and you mustn't use floats as arguments for it.
"""

a = 1234
b = 10
#shift left
a = 1234 * 10
print(a)
#shift right
a = 1234 // 10
print(a)

# >> shift right
a = 17 # 00010000
a_right = a >> 1 # 000010000
# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1)
print(a_right)

# << shift left
a_left = a << 1 # 00100000
# 17 << 2 → 17 * 2 (17 multiplied by 2 to the power of 1) → 34
print(a_left)

