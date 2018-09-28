"""
    Introduction to Machine Learning !!
    1. Supervised Learning
        Where we have data
    2. Unsupervised Learning
        We do not have data so we label the data


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

from sklearn import tree

data = [[100,70],[120,80],[150,90],[800,1000],[1000,1200],[1500,1300]]
labels = [0,0,0,1,1,1]

# Create Object of DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()
clf.fit(data,labels)

output = clf.predict([[1000,1370]])

print("Prediction is",output)
