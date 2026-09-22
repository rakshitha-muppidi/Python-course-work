# 5.Bitwise operator
a=5
b=3
print(a & b) # AND
print(a | b) # OR
print(a ^ b) # XOR
print(a << b) # Left Shift
print(a >> b) # Right Shift

# 6.Membership operators
l=[1,2,3,4,5]
target=3
print(target in l)
print(target not in l)

# 7.Identity Operator
a=[10,20]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)