import numpy as np
A = np.array([(10,20,30),(40,50,60),(70,80,90)])
print(A)
print(type(A))

print(A[1])
print(A[1][0])

# for arr in A:
#     for a in arr:
#         print(a)


B = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(B)
print(type(B))
print(B[1])

C = np.array( [[ [10,20,30],[40,50,60],[70,80,90] ] , [ [10,20,30],[40,50,60],[70,80,90] ] ])

print(C)
print(type(C))

print("Dimension of A ",A.ndim)
print("Dimension of B ",B.ndim)
print("Dimension of C ",C.ndim)

print("Shape of A ",A.shape)
print("Shape of B ",B.shape)
print("Shape of C ",C.shape)

print("Size of A ",A.__sizeof__())
print("Size of A ",A.size)

print("Size of B ",B.__sizeof__())
print("Size of B ",B.size)

print("Size of C ",C.__sizeof__())
print("Size of C ",C.size)

print("DataType of A ",A.dtype)


P = np.array([(10, 20, 30),(40, 50, 60)])
print(P)
print(P.shape)

# Arrays are IMMUTABLE
# We cannot reshape an existing Array
# Reshaping an Array will generate a new Array
Q = P.reshape(3,2)

print(P)
print(P.shape)

print("---------")

print(Q)
print(Q.shape)


