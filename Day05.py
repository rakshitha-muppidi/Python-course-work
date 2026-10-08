# strings and formatting
#String-Sequence of characters written inside the quotes- which is immutable data type-we can do slicing
#Sring operations
# 1.String concatenation

str1="python"
str2="programming"
print(str1 + " " + str2)

# 2.string repetition
a="abc"
print(a * 3)

# 3.string comparison
print('abc' > 'ABC')

# String Methods
name=" Rakshitha Muppidi  "
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name.replace('R','r'))
print(name.split())
print(name.join(","))
print(name.find("a"))
print(name.index("k"))

# check methods
name="rakshitha"
print(name.islower())
print(name.isupper())
print(name.isalpha())
print(name.isdigit())
print(name.isspace())
print(name.istitle())
#find()
x="banana"
res=x.rfind("a")-x.find("a")+x.count("a")
print(res)

# formatting
# 1.Input Formatting
name="Rakshitha"
print(name)
# 2.Output formatting
name="Rakshitha"
age=23
print(name,age)

# 3.Modulo formatting
name="Rakshitha"
print("My name is %s" % name)

name=22
print("I am %d years old % age")
# float
price=99.5
print("Price is %f" % price)
# float 2-decimal places
price= 99.5678
print("Price is %.2f" % price)

# f-strings
name="Rakshitha"
age=23
print(f"My name is {name} and I am 23 years old")

a=10
b=20
print(f"sum={a+b}")

# dot.formatting
# 1. .format() method uses {} as placeholders
name="Rakshitha"
age=23
print("My name is {} and I am {} years old".format(name,age))

# 2. position based format
name="Rakshitha"
age=23
print("My name is {0} and I am {1} years old".format(name,age))

# 3.reusing a value
name="Rakshitha"
print("{0} is learning python. {0} likes python.".format(name))

# named formatting
print("My name is {name} and I am {age} years old".format(name="Rakshitha", age=23))







