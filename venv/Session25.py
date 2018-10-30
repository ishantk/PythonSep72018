import matplotlib.pyplot as plt
from scipy import stats

X = [1, 2, 3,4 , 5]
Y = [2, 4, 5, 4, 5]

data = stats.linregress(X,Y)
print(data[0]) # b1 -> Slope
print(data[1]) # b0

plt.plot(X,Y,"ro")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


"""
Machine Learning:
	Linear Regression: 
	y = mx + c
	y = b0x + b1


	1. To Predict
	2. We need data i.e. its gonna work for supervised training model

	2002	100
	2003    200
	2005    350
	2008    ?


	X     Y
	1     2
	2     4
	3     5
	4     4
	5     5

	Mean X (X') : 3
	Mean Y (Y') : 4

	Calculate Distance of each point from the mean
	
	X     Y    X-X'   Y-Y'  square(X-X')   (X-X')(Y-Y')
	1     2    -2 	  -2    4 				4
	2     4    -1 	   0	1 				0
	3     5     0      1    0				0
	4     4     1      0    1 				0
	5     5     2      1    4   			2
							------------------
							10 				6

			y = b0 +b1x
			b1 = 6/10
			b1 = 0.6

			4 = b0 + (0.6)(3)
			b0 = 2.2


			y = 2.2 + 0.6(x)

			X is Data which we have already
			Y is Prediction

"""
# Do Mathematics for Prediction | OOPS
# Read Any CSV File to predict
# Predict how will a Singer perform in upcoming year(s)
# WebScrap Data form Website -> Convert it to CSV File -> Analyze the same to predict