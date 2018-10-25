# Generator

# def sayHello():
#     return "Hello"
#
# s = sayHello()

def sayHello():
    yield "Hello"
    yield "Hi"
    yield "Hola"
    yield "Bonjour"
    yield "Bye"

s = sayHello()

print(s)
print(type(s))

# Use Generator
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# StopIteration After this
# print(next(s))

print("**********")

def dataGenerator():
    file = "studentsData.csv"
    for row in open(file,"r"):
        yield row

dg = dataGenerator()
print(type(dataGenerator))
print(type(dg))

print("**********")
# print(next(dg))
# print(next(dg))

print(next(dg))
print("**********")
for data in dg:
    print(data)
