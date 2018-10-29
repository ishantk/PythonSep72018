
print("==App Started==")

a = 10
b = 0
c = 0
names = ["John","Jennie","Jim","Jack","Joe"]
print(names[2])

try:
    print(names[3])
    c = a / b
except Exception as e: # Because Exception is Parent to all the Exception Classes
    print("Some Error Occurred !! ",e)
    print(type(e))
finally:
    print("This is executed at any cost !!")
# except ZeroDivisionError as zRef:
#     print("Some ZeroDivisionError Occurred !! ", zRef)

# except IndexError as iRef:
#     print("Some Error Occurred")

print("c is",c)

print("==App Finished==")
