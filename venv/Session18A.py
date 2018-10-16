import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

print("Pandas Version:",pd.__version__)
print("MatPlot Version:",matplotlib.__version__)
print("Python Version:",sys.version)

"""

# DataSet : Collection of Data in a Structured Approach
streams = ["cse", "ece", "me", "ce", "ee"]
students= [120, 120, 60, 60, 90]
          # zip is zipping the 2 different lists
          # list() constructor
dataSet = list(zip(streams,students))
print(dataSet)

for data in dataSet:
    print(data)

print("*************")
df = pd.DataFrame(data=dataSet,columns=["Streams","Students"])
print(df)

df.to_csv("studentsData.csv",index=False,header=False)
print("==Data Written in File==")

"""
# df = pd.read_csv("studentsData.csv")
# df = pd.read_csv("studentsData.csv", header=None)
df = pd.read_csv("studentsData.csv", names=["Streams","Students"])

print(df)
print("*********")
print(df.dtypes)

print("*********")
# sortedDf = df.sort_values(["Streams"],ascending=True)
sortedDf = df.sort_values(["Students"],ascending=True)
print(sortedDf)

print("***************")
# print(sortedDf.head(1))
print(sortedDf.head(2))

print("***************")
print("Maximum Students:",sortedDf["Students"].max())

print("************")
plt.plot(df["Streams"],df["Students"])
plt.title("College Data 2018")
plt.xlabel("Streams")
plt.ylabel("Students")
plt.show()
