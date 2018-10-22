import numpy as np
A = np.linspace(1,5,10)
# print(A)
for elm in A:
    print(elm)


B = np.array([10,20,30,40,50])
print("Max in B is:",B.max())
print("Min in B is:",B.min())
print("Sum of Elements in B is:",B.sum())

X = np.array([[1,1,1],[2,2,2]])
Y = np.array([[3,3,3],[4,4,4]])

print("Shape of X is:",X.shape)
print("Shape of Y is:",Y.shape)

Z = X + Y
print(Z)

P = np.array([[1,2,3],[4,5,6]])
Q = np.array([[9,8,7],[3,2,1]])

# Vertical Stacking of Arrays
R = np.vstack((P,Q))
print("****************")
print(R)
print(R.shape)
print("****************")

# Horizontal Stacking of Arrays
S = np.hstack((P,Q))
print("****************")
print(S)
print(S.shape)
print("****************")

T = np.array([[1,2,3],[4,5,6]])
# U = np.square(T)
U = np.sqrt(T)
print(T) # No Change in T
print(U) # New Array Created