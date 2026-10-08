# conditional statements problems
# if-elif-else statement - FizzBuzz problem
a=int(input())
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a %3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
else:
    print(a,"is not divisible by 3 or 5")

#if-elif-else statement - Grade problem 
year=int(input())
if year%400 == 0:
    print(year,"is a leap year")
elif year%100 == 0:
    print(year,"is not a leap year")
elif year%4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")    

# greatest among three numbers problem
a,b,c=map(int,input().split())
if a == b == c:
    print("All numbers are equal")
elif a ==b:
    if a >b:
        print(a)
    else:
        print(b)
elif b == c:
    if b > c:
        print(b)
    else:
        print(c)
elif a == c:
    if a > b:
        print(a)
    else:
        print(b)
elif a >b and b>c:
    print(a)
elif b>a and a>c:
    print(b)
elif c>a and a>b:
    print(c)
















# nested-if statement - Leap year problem
year=int(input())
leap=False
if year%4==0:
    if year%100==0:
        if year%400==0:
            leap=True
        else:
            leap=False
    else:
        leap=True
else:
    leap=False
print(leap)


