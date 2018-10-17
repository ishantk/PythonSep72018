from matplotlib import pyplot as plt

# Bar Graph

A = [0.25, 1.25, 2, 2.25, 3, 3.25, 4.50]
B = [30, 40, 50, 60, 70, 90, 80]

plt.bar(A, B, label="Indian Literacy", width=0.5)

P = [0.75, 2.25, 3, 3.25, 4, 5.25, 5.50]
Q = [80, 40, 70, 60, 70, 90, 80]

plt.bar(P, Q, label="UK Literacy", width=0.5)

plt.legend()

plt.xlabel("Qualified Citizens")
plt.ylabel("Jobs")

plt.title("Literacy Survey")

plt.show()