# Creating Functions in Python
def hello():
    print("Hello, This is an Awesome Day !")

def bye():
    print("Bye, It was a great Day !")

def addNums(a, b):
    c = a+b
    print("c is",c)

hello()
bye()

# Assign references to functions
f1 = hello
f2 = bye
f3 = addNums
print("==========")
f1()
f2()
f3(10,20)

print("==========")

# Nested Functions in Python
def outer():
    print("This is outer !!")

    def inner():
        print("This is inner !!")

    inner()

outer()

# Functions Returning References to other Functions
def myOuter():
    print("This is my outer !!")

    def myInner():
        print("This is my inner !!")

    return myInner  # Returing Ref of myInner method

print("==========")

f4 = myOuter()
f4()

# Functions Returning References to other Functions with data as inputs
def yourOuter(a):
    print("This is your outer !! and a is",a)

    def yourInner1(b):
        print("This is your inner1 !! and b is",b)

    def yourInner2(b):
        print("This is your inner2 !! and b is",b)

    if a > 50:
        return yourInner1  # Returing Ref of yourInner method
    else:
        return yourInner2

print("==========")

f5 = yourOuter(100)
f5(200)

print("==========")


# Functions taking reference to function as input
# Functions returning reference to function as well

def ourOuter(fun):
    print("This is our outer function")

    def ourInner():
        print("==Our Inner Started==")
        fun()
        print("==Our Inner Finished==")

    return ourInner

@ourOuter
def sayHello():
    print("This is hello from ATPL")

# ourOuter(sayHello)

# Below writter statements are now replaced with just a single sayHello Call
# f6 = ourOuter(sayHello)
# f6()
sayHello()
