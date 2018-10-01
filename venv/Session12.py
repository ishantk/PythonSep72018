#File Read Operation

"""
file = open("Session1.py","r")
print(type(file))

#Read Data
data = file.read()
print(type(data))
print(data)
"""

# file = open("/Users/ishantkumar/Downloads/myemployees.csv","r")
# data = file.read()
# print(data)

"""
line = file.readline()
print(line)

line = file.readline()
print(line)
"""

"""
data = file.read(50) # 1st 50 characters
print(data)

data = file.read()   # Read remaining data
print(data)

data = file.read()   # ?
print(data)

file.close() # Release the memory

print(file.closed)

"""

file = open("/Users/ishantkumar/Downloads/myemployees.csv","r")
lines = file.readlines()

print(lines)
print(type(lines)) #list

# print(lines[0])
# print(lines[1])

for line in lines:
    print(line)