import time
import numpy as np

# A = [10,20,30,40,50,60,70,80,90,100]
A = list(range(100))
print(A)

B = np.array([10,20,30,40,50,60,70,80,90,100])
C = np.array((10,20,30,40,50,60,70,80,90,100))
print(B)
print(C)

print(type(B))
print(type(C))

D = np.arange(100)
print(D)
print(type(D))

startTime1 = time.time()
for elm in A:
    print(elm)
endTime1 = time.time()


startTime2 = time.time()
for elm in D:
    print(elm)
endTime2 = time.time()


timeTaken1 = endTime1 - startTime1
timeTaken2 = endTime2 - startTime2

print("Type of A",type(A))
print("Type of D",type(D))

print("Size of A is",A.__sizeof__())      #Memory -> More
print("Size of D is",D.__sizeof__())      #Memory -> Less

print("ST: {}, ET: {} Time Taken to Print A is".format(startTime1,endTime1),timeTaken1) #Time
print("ST: {}, ET: {} Time Taken to Print D is".format(startTime2,endTime2),timeTaken2) #Time