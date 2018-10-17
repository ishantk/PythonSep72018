from matplotlib import pyplot as plt

# Scatter Graph

X1 = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
Y1 = [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]


X2 = [9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 14.5, 15]
Y2 = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]

plt.scatter(X1, Y1, label="Flipkart", color='r')
plt.scatter(X2, Y2, label="Amazon", color='g')

plt.title("E-Commerce Sales")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.legend()

plt.show()
