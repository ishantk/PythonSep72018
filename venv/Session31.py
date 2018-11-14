import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets.samples_generator import make_blobs

# Engineers
X1 = [1, 2, 3, 4, 5]                        # Years of Work Experience
Y1 = [20000, 25000, 37000, 53000, 65000]    # Monthly Income

# Doctors
X2 = [1, 2, 3, 4, 5]                        # Years of Work Experience
Y2 = [33000, 46000, 58000, 68000, 75000]    # Monthly Income

plt.scatter(X1, Y1, c='r', s=30, label="SE")
plt.scatter(X2, Y2, c='g', s=30, label="DO")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc=1)
plt.show()

# SVM Demo using SciKit

X, Y = make_blobs(n_samples=40, centers=2, random_state=20)

print(X)
print(Y)

clf = svm.SVC(kernel="linear", C=1)

clf.fit(X,Y)

plt.scatter(X[:,0], X[:,1], c=Y, s=30, cmap=plt.cm.Paired)
plt.show()

# Solve IRIS DataSet using SVM