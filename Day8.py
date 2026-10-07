# conditional statements - allows us to execute a block of code based on a condition
# 1. if statement - executes a block of code if the condition is true
# syntax:
# if condition:
#     block of code
x=10
if x>5:
    print("x is greater than 5")

# 2. if-else statement - executes one block of code if the condition is true, and another block if it's false
# syntax:
# if condition:
#     block of code
# else:
#     block of code
y=3
if y>5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# 3. if-elif-else statement - allows us to check multiple conditions
# syntax:
# if condition1:
#     block of code
# elif condition2:
#     block of code
# else:
#     block of code
z=7
if z>10:
    print("z is greater than 10")
elif z>5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is not greater than 5")

#4. nested if statement - allows us to check multiple conditions within another condition
# syntax:
# if condition1:
#     if condition2:    
#        block of code
      # else:
#        block of code
# else:
#     block of code
age=20
if age>=18:
    if age>=21:
        print("You are allowed to drink alcohol")
    else:
        print("You are not allowed to drink alcohol") 
else:
    print("You are not allowed to drink alcohol")
    