# Loops problems
# printing multiplication table
num=int(input())
for i in range(1,11):
    print(num, "X", i, "=", num*i)
# even number
n=int(input())
for i in range(n):
    if i % 2 == 0:
        print(i, "is divisible by 2")
    else:
        print("Not divisible by 2")  

# sum of numbers from 1 to 10
total=0
for i in range(1,11):
    total+=i
print(total)  

# factorial
num=int(input())
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

# count the number of digits
n=12345
count=0
while n>0:                           
    n // 10
    count += 1
print(count)

# reversing a number
num=int(input())
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10+digit
    num//=10

print(rev)

# sum of even numbers from 1 to 100
sum=0
for i in range(1,101):
    if i % 2 == 0:
        sum+=i 
print(sum)

# check whether a num is palindrome
# find the sum of digits
# count even and  odd digits
