# CONTROL STATEMENTS
# 1.Conditional statements - allows us to execute a block of code based on a condition
# 2.Loops - allows us to execute a block of code multiple times
# 1.for
# 2.while
# 3.Jumping/Transfer statements-(break,continue)

# 2.loops-for loop
# syntax:
# for variable in sequence:
    # statement

for i in range(1,6):
    print(i)

# while
# syntax:
# while condition:
    # statement

i=1
while i <=5:
    print(i)
    i+=1

# 3.jumping statements
# break-completely stops the loop
for i in range(1,11):
    if i==5:
        break
    print(i)

# continue-skips the current iteration and moves to the next iteration.
for i in range(1,6):
    if i == 3:
        continue
    print(i)

#pass-it is used as placeholder when u want to write the structure but don't want to implement it yet.
for i in range(5):
    pass
# nothings happens 