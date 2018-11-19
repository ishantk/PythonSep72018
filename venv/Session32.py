"""
    Classification Problem
    Engine (X)      Weight (Y)         Vehicle (Z)
    100cc           70kgs              Bike
    120cc           80kgs              Bike
    150cc           90kgs              Bike

    800cc           1000kgs            Car
    1000cc          1200kgs            Car
    1500cc          1300kgs            Car

    85cc            85kgs              Bike


    Bike - 0
    Car  - 1


    Algorithm : DecisionTree
    3 libraries are required:
    1. numpy
    2. scipy
    3. scikit-learn
"""

from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([[100,70],[120,80],[150,90],[800,1000],[1000,1200],[1500,1300]])
Y = np.array([0,0,0,1,1,1])

model = GaussianNB()
model.fit(X,Y)

newData = [110,88]

lbl = model.predict([newData])

print("Prediction is:",lbl)


