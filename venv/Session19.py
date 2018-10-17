from matplotlib import pyplot as plt

# Draw a Line Graph
# Multiple Lines in the Same Graph

X1 = [5, 9, 11]
Y1 = [12, 15, 17]

X2 = [6, 13, 16]
Y2 = [3, 2, 1]

plt.plot(X1,Y1,'g', label="Category-A", linewidth=3)
plt.plot(X2,Y2,'c', label="Category-B", linewidth=5)

plt.legend()

plt.title("Data")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True,color='g')

plt.show()
