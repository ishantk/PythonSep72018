import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("advertising.csv")
# print(data)

X = data["TV"].values
Y = data["Sales"].values

print(">>>>>>>>>>>>>>>X><<<<<<<<<<<<<<<")
print(X)
print(">>>>>>>>>>>>>>>>Y<<<<<<<<<<<<<<<")
print(Y)
print(">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<")

result = stats.linregress(X,Y)
b1 = result[0]
b0 = result[1]

print("Slope is:",b1)
print("Intercept is:",b0)

# Equation: Y = b0 + b1.X

# Predict Y1 based on equation of line for original values of X

Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)

print(">>>>>>>>>>>>>>>>Y1<<<<<<<<<<<<<<<")
print(Y1)
print(">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<")

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
# plt.plot(X,Y,"ro")
plt.plot(X, Y, "o", X, Y1)
# plt.show()

# Calculating MSE will help us to know wether we have correct equation or not to predict

print(">>>>>>>>>>>>>>>>SCI-KIT<<<<<<<<<<<<<<<")

# Let us USE SCIPY to Solve Linear Regression Problem
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create Object of Linear Regression
regression = LinearRegression()

l = len(X)
X = X.reshape(l,1)

print(l)
print("************")
print(X)
print("************")
            # fit is a function which is taking data as input
            # this input data is also know as training data
regResult = regression.fit(X, Y)

Y1 = regResult.predict(X)
print("=======================")
print(Y1)
print("=======================")
mse = regResult.score(X,Y)
print("=======================")
print("MSE:",mse)
print("=======================")