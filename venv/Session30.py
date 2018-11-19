from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
print("=====================")
print(iris)
print("=========DATA============")
print(iris.data)
print("===========TARGET==========")
print(iris.target)


clf = tree.DecisionTreeClassifier()

# Training the ML Model | Supervised Learning
clf = clf.fit(iris.data,iris.target)

inputData = [6.0, 3.2, 5.3, 1.9]
predictedClass = clf.predict([inputData])

print("Flower Type is:",predictedClass)


import graphviz

# data = tree.export_graphviz(clf,out_file=None)
data = tree.export_graphviz(clf,out_file=None,feature_names=iris.feature_names,class_names=iris.target_names,filled=True,rounded=True,special_characters=True)
graph = graphviz.Source(data)
graph.render("iris")

graph.view()
