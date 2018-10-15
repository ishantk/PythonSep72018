names = ["John","Jennie","Jim","Jack","Joe"]
print(names[1])
print(names[1:3])
print(names[-3])

# Iterate in List
print("==================")
for i in range(0,len(names)):
    print(names[i])

print("==================")

print("==================")
for name in names:      # For-Each Loop or Enhanced For Loop
    print(name)
print("==================")

if "Mike" in names:
    print("Mike is in the list")
else:
    print("Mike is not in the list")

names.append("Mike")
names.append("Leo")
names.append("Fionna")

print(names)

names.insert(1,"Kia")
print(names)

names.remove("Jim")
print(names)

# names.clear()
# print(names)

names.pop()

print(names)

"""
HW:
Stack of Integer Numbers.
Thread1 will push the data
Thread2 will pop the data

Thread1 and Thread2 will work on same object of Stack, Implement Synchronization

Read the file anc put the found data in lists.

"""