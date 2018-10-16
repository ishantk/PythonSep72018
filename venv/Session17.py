str1 = "Hello"
str2 = 'Hello'

print("str1 hex id is",hex(id(str1)))
print("str1 hex id is",hex(id(str2)))

a = 10
b = 10

print("a hex id is",hex(id(a)))
print("b hex id is",hex(id(b)))

# Literal is created once and not re-created

str3 = """
    I can write anything of my choice.
    The way i will write, it will be added
"""

print("str1 is",str1)
print("str2 is",str2)
print("str3 is",str3)

# Reference Comparison
if str1 == str2:
    print("str1 is equal to str2")

# Strings or Literal are IMMUTABLE
# Any operation on String will result into a new String
str4 = str1.upper()

print("str1 now is",str1)
print("str4 now is",str4)

names = "John, Jennie, Jim, Jack, Joe"

# String Slicing
print(names[0])
print(names[7])
print(names[7:])
print(names[7:10])
print(names[:7])
print(names[:])
print(names[-1])

print("Names",names[-3])
print("Names",names[-7:-1])

newNames = names.split(",")
print(newNames)
print(type(newNames))

for nm in newNames:
    print(nm.strip())

# names = "John, Jennie, Jim, Jack, Joe"
print(len(names))
newNamesAgain = names.replace('J','K')
print(newNamesAgain)

email = "john@example.com"
phone = "9999988888"

# if email.endswith(".com"):
if email.__contains__("@") and email.__contains__("."):
    print("A valid Email")
else:
    print("Invalid Email")

if len(phone) is 10:
    print("Correct Phone Number")
else:
    print("Please enter 10 digits")

print(names.__contains__("John"))


""" 
HW:Source Code Analysis
1. Read a Python Source File.
2. Count all the references in source code     -> list1
3. Count all the literals in source code       -> list2
4. Count how many if/else used in source code  -> list3
5. Count how many times we printed some output -> list4   
"""