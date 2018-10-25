"""
def add(a=10, b=20):
    return (a+b)

c = add()
print("c is",c)
"""

def squareOfNum(num):
    return num*num

fun = squareOfNum # Reference Copy

print("Square of 5 is",squareOfNum(5))
print(type(squareOfNum))
print(hex(id(squareOfNum)))

print("Square of 9 is",fun(9))
print(type(fun))
print(hex(id(fun)))

print("************")

# Lambdas | Anonymous Functions | Single Line Funcions

myFun = lambda x, y : x * y
print("Multiplication of 13 and 15 is",myFun(13,15))
print(type(myFun))
print(hex(id(myFun)))

yourFun = lambda x,y,z : x+y+z
print(yourFun(10,20,30))

print("**************")

# Maps

def square(num1, num2, num3):
    return num1 * num2 * num3

l1 = lambda num1, num2, num3 : num1 * num2 * num3

# m1 = map(square,[1,2,3,4,5],[6,7,8,9,1],[9,8,7,6,5])
m1 = map(l1,[1,2,3,4,5],[6,7,8,9,1],[9,8,7,6,5])
print(m1)
print(type(m1))
print(hex(id(m1)))
myList = list(m1)
print(myList)

print("**************")

# List of Dictionaries
employees = [ {"eid":101,"name":"John"},{"eid":201,"name":"Jennie"},{"eid":301,"name":"Fionna"}, {"eid":401,"name":"John"} ]

# Lambda to print eid of Employee
lmEmpIds = lambda dic : dic["eid"]

# Lambda to print wether employee is John or Not
lmEmpJohn = lambda dic : dic["name"] == "John"

result = map(lmEmpIds,employees)
# result = map(lmEmpJohn,employees)
eIdList = list(result)
print(eIdList)

print("**************")

lmAddLists = lambda P, Q : P + Q
L1 = [10, 20, 30, 40, 50]
L2 = [10, 10, 10, 10, 10]

result = map(lmAddLists,L1,L2)
print(list(result))

print("**************")

L3 = [10,20,30,40,50,11,12,13,14,15]
lmEvenCheck = lambda n : n%2 == 0
result = map(lmEvenCheck,L3)
print(list(result))

# Filters
filterResult = filter(lmEvenCheck,L3)
print(list(filterResult))

print("**************")
# Filter on Dictionary
filteredEmployees = filter(lmEmpJohn,employees)
print(list(filteredEmployees))

# List Comprehensions
A = [10,20,30,40,50]
B = [x*x for x in [1,2,3,4,5]]
C = [x*x for x in [1,2,3,4,5] if x%2==0]

print("**************")
print(A)
print(B)
print(C)
